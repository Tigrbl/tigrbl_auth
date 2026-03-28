"""Compatibility facade for canonical RFC 9101 JAR helpers.

The canonical standards implementation keeps temporal claims like ``iat`` and
``exp`` in parsed payloads. This legacy facade strips auto-managed temporal
claims to preserve the historical checkpoint helper contract expected by older
unit tests.
"""

from __future__ import annotations

from typing import Any, Iterable

from tigrbl_auth.standards.oauth2.rfc9101 import (
    RFC9101_SPEC_URL,
    OWNER,
    STATUS,
    StandardOwner,
    describe,
)
from tigrbl_auth.standards.oauth2 import rfc9101 as _canonical


async def make_request_object(
    params: dict[str, Any],
    *,
    secret: str,
    algorithm: str = "HS256",
) -> str:
    return await _canonical.make_request_object(params, secret=secret, algorithm=algorithm)


async def makeRequestObject(
    params: dict[str, Any],
    *,
    secret: str,
    algorithm: str = "HS256",
) -> str:
    return await make_request_object(params, secret=secret, algorithm=algorithm)


async def create_request_object(
    params: dict[str, Any],
    *,
    secret: str,
    algorithm: str = "HS256",
) -> str:
    return await makeRequestObject(params, secret=secret, algorithm=algorithm)


async def parse_request_object(
    token: str,
    *,
    secret: str,
    algorithms: Iterable[str] | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    payload = await _canonical.parse_request_object(
        token,
        secret=secret,
        algorithms=algorithms,
        **kwargs,
    )
    return {
        key: value
        for key, value in payload.items()
        if key not in {"iat", "exp"}
    }


__all__ = [
    "STATUS",
    "RFC9101_SPEC_URL",
    "StandardOwner",
    "OWNER",
    "make_request_object",
    "makeRequestObject",
    "create_request_object",
    "parse_request_object",
    "describe",
]
