"""Compatibility facade for canonical RFC 7523 JWT client-auth helpers."""

from tigrbl_auth.standards.oauth2.jwt_client_auth import (
    CLIENT_SECRET_JWT_AUTH_METHOD,
    JWT_BEARER_ASSERTION_TYPE,
    PRIVATE_KEY_JWT_AUTH_METHOD,
    RFC7523_SPEC_URL,
    authenticate_client_assertion,
    build_client_assertion_contract_examples,
    make_client_assertion_jwt,
    token_endpoint_auth_methods_supported,
    token_endpoint_auth_signing_alg_values_supported,
    validate_client_jwt_bearer,
)

__all__ = [
    "PRIVATE_KEY_JWT_AUTH_METHOD",
    "CLIENT_SECRET_JWT_AUTH_METHOD",
    "JWT_BEARER_ASSERTION_TYPE",
    "authenticate_client_assertion",
    "build_client_assertion_contract_examples",
    "make_client_assertion_jwt",
    "token_endpoint_auth_methods_supported",
    "token_endpoint_auth_signing_alg_values_supported",
    "validate_client_jwt_bearer",
    "RFC7523_SPEC_URL",
]
