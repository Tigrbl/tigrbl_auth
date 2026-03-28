from __future__ import annotations

import json
from urllib.parse import parse_qs
from uuid import UUID

from tigrbl_auth.config.deployment import resolve_deployment
from tigrbl_auth.config.settings import settings
try:  # pragma: no cover - exercised with the full runtime stack installed
    from tigrbl_auth.services.persistence import append_audit_event_async
except Exception:  # pragma: no cover - dependency-light fallback for checkpoint tests/evidence
    async def append_audit_event_async(**kwargs):
        return None
from tigrbl_auth.standards.oauth2.jar import merge_request_object_params, parse_request_object
from tigrbl_auth.standards.oauth2.par import REQUEST_URI_PREFIX
from tigrbl_auth.standards.oauth2.rar import normalize_authorization_details
from tigrbl_auth.standards.oauth2.resource_indicators import select_resource_indicator

try:  # pragma: no cover - exercised with the full runtime stack installed
    from tigrbl_auth.framework import HTTPException, select, status
except Exception:  # pragma: no cover - dependency-light fallback for checkpoint tests/evidence
    class _FallbackStatus:
        HTTP_400_BAD_REQUEST = 400
        HTTP_404_NOT_FOUND = 404

    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: object):
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail

    class _Select:
        def __init__(self, model: object):
            self.model = model
            self.criteria: list[object] = []

        def where(self, criterion: object):
            self.criteria.append(criterion)
            return self

    def select(model: object):
        return _Select(model)

    status = _FallbackStatus()

try:  # pragma: no cover - exercised with the full runtime stack installed
    from tigrbl_auth.tables import Client, PushedAuthorizationRequest
except Exception:  # pragma: no cover - dependency-light placeholders
    class Client:  # type: ignore[override]
        id = object()
        tenant_id = None

    class PushedAuthorizationRequest:  # type: ignore[override]
        def __init__(self, *, client_id=None, tenant_id=None, params=None):
            self.id = 'dependency-light-par-row'
            self.client_id = client_id
            self.tenant_id = tenant_id
            self.params = dict(params or {})
            self.request_uri = f'{REQUEST_URI_PREFIX}dependency-light'
            self.expires_in = 90
            self.expires_at = None
            self.consumed_at = None



def _body_dict(body: bytes) -> dict:
    if not body:
        return {}
    text = body.decode('utf-8')
    try:
        parsed_json = json.loads(text)
        if isinstance(parsed_json, dict):
            return parsed_json
    except Exception:
        pass
    parsed = parse_qs(text, keep_blank_values=True)
    result: dict[str, object] = {}
    for key, values in parsed.items():
        if len(values) == 1:
            result[key] = values[-1]
        else:
            result[key] = list(values)
    return result


async def _normalized_par_params(params: dict[str, object], deployment) -> dict[str, object]:
    normalized = dict(params)
    request_object = normalized.get('request')
    if request_object:
        if not deployment.flag_enabled('enable_rfc9101'):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'request object support disabled')
        try:
            parsed_request = await parse_request_object(
                str(request_object),
                secret=settings.jwt_secret,
                algorithms=('HS256', 'HS384', 'HS512'),
                expected_client_id=str(normalized.get('client_id') or '') or None,
                expected_audience=str(deployment.issuer or settings.issuer),
            )
            normalized = merge_request_object_params(parsed_request, normalized, allow_query_overrides=('request',))
        except Exception as exc:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'invalid request object') from exc

    resources = normalized.get('resource')
    if resources not in (None, '', [], (), {}):
        values = resources if isinstance(resources, list) else [resources]
        if not deployment.flag_enabled('enable_rfc8707'):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'resource indicators disabled')
        try:
            selection = select_resource_indicator([str(item) for item in values], audience=str(normalized.get('audience') or '') or None)
        except ValueError as exc:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'invalid_target') from exc
        normalized['resource'] = list(selection.resources)
        if selection.audience:
            normalized['audience'] = selection.audience

    authorization_details = normalized.get('authorization_details')
    if authorization_details not in (None, '', [], (), {}):
        if not deployment.flag_enabled('enable_rfc9396'):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'authorization_details disabled')
        try:
            binding = normalize_authorization_details(
                authorization_details,
                resource=str(normalized.get('audience') or '') or None,
                audience=str(normalized.get('audience') or '') or None,
            )
        except Exception as exc:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'invalid authorization_details') from exc
        normalized['authorization_details'] = binding.details
        if binding.audience and normalized.get('audience') in {None, ''}:
            normalized['audience'] = binding.audience
        if binding.resource and normalized.get('resource') in (None, '', [], (), {}):
            normalized['resource'] = [binding.resource]
    return normalized


async def pushed_authorization_request(*, request, db):
    deployment = resolve_deployment(settings)
    if not deployment.flag_enabled('enable_rfc9126'):
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'PAR disabled')
    params = _body_dict(getattr(request, 'body', b'') or b'')
    params = await _normalized_par_params(params, deployment)
    client_id = params.get('client_id')
    if not client_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'client_id parameter required')
    try:
        client_uuid = UUID(str(client_id))
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'invalid client_id') from exc
    client = await db.scalar(select(Client).where(Client.id == client_uuid))
    if client is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'client not found')

    row = PushedAuthorizationRequest(
        client_id=client.id,
        tenant_id=client.tenant_id,
        params=params,
    )
    db.add(row)
    await db.commit()
    try:
        await db.refresh(row)
    except Exception:
        pass

    await append_audit_event_async(
        tenant_id=client.tenant_id,
        actor_client_id=client.id,
        event_type='authorization.par.created',
        target_type='par_request',
        target_id=str(row.id),
        details={
            'request_uri': row.request_uri,
            'resource': params.get('resource'),
            'audience': params.get('audience'),
            'authorization_details_present': bool(params.get('authorization_details')),
            'request_object_present': bool(params.get('request')),
        },
    )

    return {'request_uri': row.request_uri, 'expires_in': row.expires_in}
