from __future__ import annotations

from uuid import UUID

from tigrbl_auth.framework import HTTPException, Request, status

from tigrbl_auth.services.token_service import JWTCoder
from tigrbl_auth.services.auth_backends import PasswordBackend
from tigrbl_auth.config.settings import settings
from tigrbl_auth.standards.oidc.frontchannel_logout import mark_frontchannel_complete
from tigrbl_auth.standards.oidc.backchannel_logout import mark_backchannel_complete

_jwt = JWTCoder.default()
_pwd_backend = PasswordBackend()

_ALLOWED_GRANT_TYPES = {"password", "authorization_code", "client_credentials"}
if settings.enable_rfc8628:
    _ALLOWED_GRANT_TYPES.add("urn:ietf:params:oauth:grant-type:device_code")


def _require_tls(request: Request) -> None:
    scope = getattr(request, "scope", {})
    scheme = scope.get("scheme") if isinstance(scope, dict) else None
    if not scheme:
        try:
            url = request.url
            scheme = url.scheme if hasattr(url, "scheme") else str(url).split(":", 1)[0]
        except Exception:
            scheme = "http"
    if settings.require_tls and scheme != "https":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, {"error": "tls_required"})


async def _front_channel_logout(logout_id: str) -> None:
    try:
        await mark_frontchannel_complete(UUID(logout_id))
    except Exception:
        return None


async def _back_channel_logout(logout_id: str) -> None:
    try:
        await mark_backchannel_complete(UUID(logout_id))
    except Exception:
        return None
