"""Domain-organized OAuth 2.0 token introspection support.

The canonical implementation uses durable persistence and the Tigrbl runtime.
When those dependencies are not importable, a dependency-light checkpoint
fallback is used so standards helpers, docs generation, and targeted tests can
still execute.
"""

from __future__ import annotations

from http import HTTPStatus as _HTTPStatus
from typing import Any, Dict, Final
from urllib.parse import parse_qs

from tigrbl_auth.config.settings import settings

try:  # pragma: no cover - exercised when the full runtime stack is installed
    from tigrbl_auth.api.rest.schemas import IntrospectOut
    from tigrbl_auth.api.rest.shared import _require_tls
    from tigrbl_auth.framework import HTTPException, Request, TigrblApp, TigrblRouter, status
    from tigrbl_auth.services.persistence import (
        introspect_token as _introspect_token,
        record_token as _record_token,
        reset_token_state as _reset_token_state,
        unregister_token as _unregister_token,
    )
except Exception:  # pragma: no cover - dependency-light checkpoint fallback
    IntrospectOut = dict  # type: ignore[assignment]

    def _require_tls(_request: Any) -> None:
        return None

    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: str):
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail

    class _Status:
        HTTP_404_NOT_FOUND = int(_HTTPStatus.NOT_FOUND)
        HTTP_400_BAD_REQUEST = int(_HTTPStatus.BAD_REQUEST)

    status = _Status()

    class Request:  # pragma: no cover - typing/documentation stub
        body: bytes = b""

    class _Route:
        def __init__(self, path: str):
            self.path = path
            self.path_template = path

    class TigrblRouter:
        def __init__(self):
            self.routes: list[_Route] = []

        def route(self, path: str, **_kwargs: Any):
            def _decorator(func):
                self.routes.append(_Route(path))
                return func

            return _decorator

    class TigrblApp:  # pragma: no cover - fallback stub
        def __init__(self):
            self.router = TigrblRouter()

        def include_router(self, router: TigrblRouter) -> None:
            existing = {
                getattr(route, "path", None) or getattr(route, "path_template", None)
                for route in self.router.routes
            }
            for route in router.routes:
                path = getattr(route, "path", None) or getattr(route, "path_template", None)
                if path not in existing:
                    self.router.routes.append(route)

    _TOKENS: dict[str, dict[str, Any]] = {}

    def _record_token(token: str, claims: Dict[str, Any], token_kind: str | None = None) -> str:
        payload = dict(claims)
        if token_kind is not None and "kind" not in payload:
            payload["kind"] = token_kind
        _TOKENS[token] = payload
        return token

    def _unregister_token(token: str) -> None:
        _TOKENS.pop(token, None)

    def _introspect_token(token: str) -> Dict[str, Any]:
        claims = _TOKENS.get(token)
        if claims is None:
            return {"active": False}
        return {"active": True, **claims}

    def _reset_token_state() -> None:
        _TOKENS.clear()

RFC7662_SPEC_URL: Final[str] = "https://www.rfc-editor.org/rfc/rfc7662"

api = TigrblRouter()
router = api
_FALLBACK_TOKENS: dict[str, dict[str, Any]] = {}


def register_token(token: str, claims: Dict[str, Any] | None = None) -> str:
    payload = dict(claims or {})
    _FALLBACK_TOKENS[token] = payload
    return _record_token(token, payload, token_kind=payload.get("kind"))


def unregister_token(token: str) -> None:
    _FALLBACK_TOKENS.pop(token, None)
    _unregister_token(token)


def introspect_token(token: str) -> Dict[str, Any]:
    if not settings.enable_rfc7662:
        raise RuntimeError(f"RFC 7662 support is disabled: {RFC7662_SPEC_URL}")
    payload = _introspect_token(token)
    if payload.get("active") is False and token in _FALLBACK_TOKENS:
        return {"active": True, **_FALLBACK_TOKENS[token]}
    return payload


def reset_tokens() -> None:
    _FALLBACK_TOKENS.clear()
    _reset_token_state()


@api.route("/introspect", methods=["POST"], response_model=IntrospectOut)
async def introspect(request: Request):
    _require_tls(request)
    if not settings.enable_rfc7662:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "introspection disabled")
    body = getattr(request, "body", b"") or b""
    form_data = parse_qs(body.decode("utf-8"), keep_blank_values=True)
    token_values = form_data.get("token") or []
    token = token_values[0] if token_values else None
    if not token:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "token parameter required")
    return introspect_token(token)


def include_introspection_endpoint(app: TigrblApp) -> None:
    path = "/introspect"
    routes = getattr(getattr(app, "router", None), "routes", [])
    if settings.enable_rfc7662 and not any(
        (getattr(route, "path", None) or getattr(route, "path_template", None)) == path
        for route in routes
    ):
        app.include_router(api)


include_rfc7662 = include_introspection_endpoint


__all__ = [
    "RFC7662_SPEC_URL",
    "api",
    "router",
    "register_token",
    "unregister_token",
    "introspect_token",
    "reset_tokens",
    "introspect",
    "include_introspection_endpoint",
    "include_rfc7662",
]
