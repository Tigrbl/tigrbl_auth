"""Legacy RFC 7009 import surface backed by the durable standards implementation."""

from __future__ import annotations

from tigrbl_auth.standards.oauth2.revocation import (
    RFC7009_SPEC_URL,
    api,
    include_rfc7009,
    is_revoked,
    reset_revocations,
    revoke,
    revoke_token,
    router,
)

__all__ = [
    "revoke_token",
    "is_revoked",
    "reset_revocations",
    "include_rfc7009",
    "revoke",
    "api",
    "router",
    "RFC7009_SPEC_URL",
]
