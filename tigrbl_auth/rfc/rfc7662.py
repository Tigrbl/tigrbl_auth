"""Legacy RFC 7662 import surface backed by the durable standards implementation.

When the full persistence/runtime stack is unavailable, this module falls back
to a dependency-light in-memory token registry so helper tests and checkpoint
workflows can still execute.
"""

from __future__ import annotations

from typing import Any, Final

from tigrbl_auth.config.settings import settings

RFC7662_SPEC_URL: Final[str] = "https://www.rfc-editor.org/rfc/rfc7662"

try:  # pragma: no cover - exercised when the full runtime stack is installed
    from tigrbl_auth.standards.oauth2.introspection import (
        introspect_token,
        register_token,
        reset_tokens,
        unregister_token,
    )
except Exception:  # pragma: no cover - dependency-light checkpoint fallback
    _TOKENS: dict[str, dict[str, Any]] = {}

    def register_token(token: str, claims: dict[str, Any] | None = None) -> str:
        _TOKENS[token] = dict(claims or {})
        return token

    def unregister_token(token: str) -> None:
        _TOKENS.pop(token, None)

    def introspect_token(token: str) -> dict[str, Any]:
        if not settings.enable_rfc7662:
            raise RuntimeError(f"RFC 7662 support is disabled: {RFC7662_SPEC_URL}")
        claims = _TOKENS.get(token)
        if claims is None:
            return {"active": False}
        return {"active": True, **claims}

    def reset_tokens() -> None:
        _TOKENS.clear()


__all__ = [
    "register_token",
    "unregister_token",
    "introspect_token",
    "reset_tokens",
    "RFC7662_SPEC_URL",
]
