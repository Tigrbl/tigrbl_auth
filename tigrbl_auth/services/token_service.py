"""JWT minting/verification and operator token wrappers."""

from __future__ import annotations

import asyncio
import base64
import json
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from threading import Thread
from typing import Any, Dict, Iterable, Optional, Tuple

from tigrbl_auth.errors import InvalidTokenError

from .key_management import _DEFAULT_KEY_PATH, _provider
from .session_service import (
    exchange_token_for_context,
    get_token_for_context,
    introspect_token_for_context,
    list_tokens_for_context,
    revoke_all_tokens_for_context,
    revoke_token_for_context,
)

_ACCESS_TTL = timedelta(minutes=60)
_REFRESH_TTL = timedelta(days=7)


def _load_runtime() -> dict[str, Any]:
    try:
        from tigrbl_auth.framework import ExportPolicy, FileKeyProvider, JWTTokenService, LocalKeyProvider, JWAAlg, KeyAlg, KeyClass, KeySpec, KeyUse
        from tigrbl_auth.config.settings import settings
        from tigrbl_auth.standards.oauth2.mtls import validate_certificate_binding
        from tigrbl_auth.standards.oauth2.revocation import is_revoked
        from tigrbl_auth.standards.oauth2.introspection import register_token
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("runtime token-service dependencies are unavailable") from exc
    return {
        "ExportPolicy": ExportPolicy,
        "FileKeyProvider": FileKeyProvider,
        "JWTTokenService": JWTTokenService,
        "LocalKeyProvider": LocalKeyProvider,
        "JWAAlg": JWAAlg,
        "KeyAlg": KeyAlg,
        "KeyClass": KeyClass,
        "KeySpec": KeySpec,
        "KeyUse": KeyUse,
        "settings": settings,
        "validate_certificate_binding": validate_certificate_binding,
        "is_revoked": is_revoked,
        "register_token": register_token,
    }


def _run(coro):
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    result = None

    def runner():
        nonlocal result
        result = asyncio.run(coro)

    thread = Thread(target=runner)
    thread.start()
    thread.join()
    return result


@lru_cache(maxsize=1)
def _svc() -> Tuple[Any, str]:
    runtime = _load_runtime()
    kp = _provider()
    if _DEFAULT_KEY_PATH.exists():
        kid = _DEFAULT_KEY_PATH.read_text().strip()
    else:
        spec = runtime["KeySpec"](
            klass=runtime["KeyClass"].asymmetric,
            alg=runtime["KeyAlg"].ED25519,
            uses=(runtime["KeyUse"].SIGN, runtime["KeyUse"].VERIFY),
            export_policy=runtime["ExportPolicy"].SECRET_WHEN_ALLOWED,
            label="jwt_ed25519",
        )
        ref = _run(kp.create_key(spec))
        kid = ref.kid
        _DEFAULT_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
        _DEFAULT_KEY_PATH.write_text(kid)
    service = runtime["JWTTokenService"](kp)
    return service, kid


def _header_alg(token: str) -> str:
    try:
        header_segment = token.split(".")[0]
        padded = header_segment + "=" * (-len(header_segment) % 4)
        header = json.loads(base64.urlsafe_b64decode(padded).decode())
        return str(header.get("alg", "")).lower()
    except Exception:
        return ""


class JWTCoder:
    __slots__ = ("_svc", "_kid")

    def __init__(self, arg1: Any, arg2: Any):
        runtime = _load_runtime()
        if isinstance(arg1, runtime["JWTTokenService"]) and isinstance(arg2, str):
            self._svc = arg1
            self._kid = arg2
            return
        if isinstance(arg1, (bytes, bytearray)) and isinstance(arg2, (bytes, bytearray)):
            kp = runtime["LocalKeyProvider"]()
            spec = runtime["KeySpec"](
                klass=runtime["KeyClass"].asymmetric,
                alg=runtime["KeyAlg"].ED25519,
                uses=(runtime["KeyUse"].SIGN, runtime["KeyUse"].VERIFY),
                export_policy=runtime["ExportPolicy"].SECRET_WHEN_ALLOWED,
                label="jwt_ed25519",
            )
            ref = _run(kp.import_key(spec, arg1, public=arg2))
            self._svc = runtime["JWTTokenService"](kp)
            self._kid = ref.kid
            return
        raise TypeError("JWTCoder requires (JWTTokenService, kid) or (private_pem, public_pem)")

    @classmethod
    def default(cls) -> "JWTCoder":
        svc, kid = _svc()
        return cls(svc, kid)

    async def async_sign(
        self,
        *,
        sub: str,
        tid: Optional[str] = None,
        ttl: timedelta = _ACCESS_TTL,
        typ: str = "access",
        issuer: Optional[str] = None,
        audience: Optional[Iterable[str] | str] = None,
        cert_thumbprint: Optional[str] = None,
        **extra: Any,
    ) -> str:
        runtime = _load_runtime()
        settings = runtime["settings"]
        now = datetime.now(timezone.utc)
        payload: Dict[str, Any] = {
            "sub": sub,
            "typ": typ,
            "iat": int(now.timestamp()),
            "exp": int((now + ttl).timestamp()),
            **extra,
        }
        if tid is not None:
            payload["tid"] = tid
        if getattr(settings, "enable_rfc8705", False) and cert_thumbprint is not None:
            payload["cnf"] = {"x5t#S256": cert_thumbprint}
        if getattr(settings, "enable_rfc9068", False) and typ == "access":
            effective_issuer = issuer or settings.issuer
            effective_audience = audience or settings.protected_resource_identifier
            from tigrbl_auth.standards.oauth2.jwt_access_tokens import add_jwt_access_token_claims

            payload = add_jwt_access_token_claims(payload, issuer=effective_issuer, audience=effective_audience)
            issuer = effective_issuer
            audience = effective_audience
        token = await self._svc.mint(
            payload,
            alg=runtime["JWAAlg"].EDDSA,
            kid=self._kid,
            lifetime_s=int(ttl.total_seconds()),
            subject=sub,
            issuer=issuer,
            audience=audience,
        )
        if getattr(settings, "enable_rfc7662", False):
            claims = dict(payload)
            claims.setdefault("sub", sub)
            claims.setdefault("kind", typ)
            if tid is not None:
                claims.setdefault("tid", tid)
            if issuer is not None:
                claims.setdefault("iss", issuer)
            if audience is not None:
                claims.setdefault("aud", list(audience) if isinstance(audience, (list, tuple, set)) else audience)
            runtime["register_token"](token, claims)
        return token

    def sign(self, **kwargs: Any) -> str:
        return _run(self.async_sign(**kwargs))

    async def async_sign_pair(self, *, sub: str, tid: str, cert_thumbprint: Optional[str] = None, **extra: Any) -> Tuple[str, str]:
        access = await self.async_sign(sub=sub, tid=tid, cert_thumbprint=cert_thumbprint, **extra)
        refresh = await self.async_sign(sub=sub, tid=tid, ttl=_REFRESH_TTL, typ="refresh", cert_thumbprint=cert_thumbprint, **extra)
        return access, refresh

    def sign_pair(self, **kwargs: Any) -> Tuple[str, str]:
        return _run(self.async_sign_pair(**kwargs))

    async def async_verify(self, token: str, *, cert_thumbprint: Optional[str] = None, audience: Optional[Iterable[str] | str] = None, issuer: Optional[str] = None) -> Dict[str, Any]:
        runtime = _load_runtime()
        settings = runtime["settings"]
        if _header_alg(token) == "none":
            raise InvalidTokenError("unsigned tokens are not accepted")
        try:
            payload = await self._svc.verify(token, audience=audience, issuer=issuer)
        except Exception as exc:
            raise InvalidTokenError("signature verification failed") from exc
        payload = dict(payload)
        if getattr(settings, "enable_rfc9700", False) and (audience is not None or issuer is not None):
            if payload.get("iss") in {None, "", "placeholder-issuer"}:
                raise InvalidTokenError("missing issuer")
            aud = payload.get("aud")
            if aud in {None, ""} or aud == []:
                raise InvalidTokenError("missing audience")
        cnf = payload.get("cnf") if isinstance(payload.get("cnf"), dict) else {}
        if getattr(settings, "enable_rfc8705", False) and cnf.get("x5t#S256") is not None:
            runtime["validate_certificate_binding"](payload, cert_thumbprint)
        if runtime["is_revoked"](token):
            raise InvalidTokenError("token revoked")
        return payload

    def verify(self, token: str, **kwargs: Any) -> Dict[str, Any]:
        return _run(self.async_verify(token, **kwargs))

    async def async_decode(self, token: str, *, verify_exp: bool = True, cert_thumbprint: Optional[str] = None, audience: Optional[Iterable[str] | str] = None, issuer: Optional[str] = None) -> Dict[str, Any]:
        payload = await self.async_verify(token, cert_thumbprint=cert_thumbprint, audience=audience, issuer=issuer)
        if verify_exp:
            exp = payload.get("exp")
            if exp is not None and int(exp) < int(datetime.now(timezone.utc).timestamp()):
                raise InvalidTokenError("token expired")
        return payload

    def decode(self, token: str, *, verify_exp: bool = True, cert_thumbprint: Optional[str] = None, audience: Optional[Iterable[str] | str] = None, issuer: Optional[str] = None) -> Dict[str, Any]:
        return _run(self.async_decode(token, verify_exp=verify_exp, cert_thumbprint=cert_thumbprint, audience=audience, issuer=issuer))



# -----------------------------
# Operator-plane wrappers
# -----------------------------

def parse_token_patch(raw_patch: dict[str, Any] | None) -> dict[str, Any]:
    patch = dict(raw_patch or {})
    patch.setdefault("issued_at", patch.get("iat") or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"))
    if "token_type" not in patch and "typ" in patch:
        patch["token_type"] = patch["typ"]
    return patch


def list_operator_tokens_for_context(context, *, status_filter: str | None = None, filter_expr: str | None = None, sort: str = "id", offset: int = 0, limit: int = 50):
    return list_tokens_for_context(context, status_filter=status_filter, filter_expr=filter_expr, sort=sort, offset=offset, limit=limit)


def get_operator_token_for_context(context, *, record_id: str):
    return get_token_for_context(context, record_id=record_id)


def introspect_operator_token_for_context(context, *, record_id: str):
    return introspect_token_for_context(context, record_id=record_id)


def revoke_operator_token_for_context(context, *, record_id: str):
    return revoke_token_for_context(context, record_id=record_id)


def revoke_all_operator_tokens_for_context(context, *, status_filter: str | None = None, filter_expr: str | None = None):
    return revoke_all_tokens_for_context(context, status_filter=status_filter, filter_expr=filter_expr)


def exchange_operator_token_for_context(context, *, subject_token: str | None, requested_token_type: str | None = None, audience: str | None = None, resource: str | None = None, actor_token: str | None = None, extras: dict[str, Any] | None = None):
    return exchange_token_for_context(context, subject_token=subject_token, requested_token_type=requested_token_type, audience=audience, resource=resource, actor_token=actor_token, extras=extras)


__all__ = [
    "JWTCoder",
    "exchange_operator_token_for_context",
    "get_operator_token_for_context",
    "introspect_operator_token_for_context",
    "list_operator_tokens_for_context",
    "parse_token_patch",
    "revoke_all_operator_tokens_for_context",
    "revoke_operator_token_for_context",
]
