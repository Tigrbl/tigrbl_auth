"""Compatibility facade for canonical RFC 7521 assertion helpers."""

from tigrbl_auth.standards.oauth2.assertion_framework import (
    JWT_BEARER_ASSERTION_TYPE,
    JWT_BEARER_GRANT_TYPE,
    RFC7521_SPEC_URL,
    build_assertion_contract_examples,
    validate_assertion_grant_request,
    validate_jwt_assertion,
)

__all__ = [
    "JWT_BEARER_GRANT_TYPE",
    "JWT_BEARER_ASSERTION_TYPE",
    "build_assertion_contract_examples",
    "validate_jwt_assertion",
    "validate_assertion_grant_request",
    "RFC7521_SPEC_URL",
]
