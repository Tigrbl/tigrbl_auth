"""Utilities for OAuth 2.0 Rich Authorization Requests (RFC 9396).

This legacy import surface stays dependency-light by falling back to Pydantic
when the full framework/runtime stack is unavailable.
"""

from __future__ import annotations

import json
from typing import Any, Final

try:  # pragma: no cover - exercised when the full runtime stack is installed
    from tigrbl_auth.framework import BaseModel, ValidationError
except Exception:  # pragma: no cover - dependency-light fallback for checkpoint tests
    from pydantic import BaseModel, ValidationError  # type: ignore

from ..runtime_cfg import settings

RFC9396_SPEC_URL: Final[str] = "https://www.rfc-editor.org/rfc/rfc9396"


class AuthorizationDetail(BaseModel):
    """Minimal representation of an authorization detail item."""

    type: str


def _validate_authorization_detail(item: Any) -> AuthorizationDetail:
    """Validate one authorization-detail item across Pydantic v1 and v2.

    The published certification target uses Pydantic v2, but local checkpoint
    environments may only provide the v1 API. This helper keeps the lightweight
    RFC parser truthful across both surfaces without widening the release-path
    framework boundary.
    """

    model_validate = getattr(AuthorizationDetail, "model_validate", None)
    if callable(model_validate):
        return model_validate(item)

    parse_obj = getattr(AuthorizationDetail, "parse_obj", None)
    if callable(parse_obj):
        return parse_obj(item)

    return AuthorizationDetail(**item)


def parse_authorization_details(raw: str) -> list[AuthorizationDetail]:
    """Parse the RFC 9396 ``authorization_details`` parameter."""

    if not settings.enable_rfc9396:
        raise NotImplementedError(
            f"authorization_details not enabled: {RFC9396_SPEC_URL}"
        )

    try:
        data: Any = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"authorization_details must be valid JSON: {RFC9396_SPEC_URL}"
        ) from exc

    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise ValueError(
            f"authorization_details must be an object or array: {RFC9396_SPEC_URL}"
        )

    try:
        return [_validate_authorization_detail(item) for item in data]
    except ValidationError as exc:
        raise ValueError(
            f"invalid authorization_details: {RFC9396_SPEC_URL}"
        ) from exc


__all__ = [
    "AuthorizationDetail",
    "parse_authorization_details",
    "RFC9396_SPEC_URL",
]
