from __future__ import annotations

from tigrbl_auth import framework as vendor
from swarmauri_core.key_providers import KeyAlg
from swarmauri_tokens_jwt import JWTTokenService


def test_framework_exposes_tokens_and_key_types() -> None:
    assert vendor.JWTTokenService is JWTTokenService
    assert vendor.KeyAlg is KeyAlg
