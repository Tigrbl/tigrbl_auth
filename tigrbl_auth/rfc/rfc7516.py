"""Compatibility facade for canonical RFC 7516 helpers."""

from tigrbl_auth.standards.jose.rfc7516 import (
    ACTIVE_JWE_POLICY,
    JWEPolicy,
    JWEPolicyError,
    RFC7516_SPEC_URL,
    SUPPORTED_JWE_ALG_VALUES,
    SUPPORTED_JWE_ENC_VALUES,
    decrypt_jwe,
    encrypt_jwe,
    jwe_policy_metadata,
    validate_jwe_header,
    validate_oct_key,
)

__all__ = [
    "ACTIVE_JWE_POLICY",
    "JWEPolicy",
    "JWEPolicyError",
    "RFC7516_SPEC_URL",
    "SUPPORTED_JWE_ALG_VALUES",
    "SUPPORTED_JWE_ENC_VALUES",
    "decrypt_jwe",
    "encrypt_jwe",
    "jwe_policy_metadata",
    "validate_jwe_header",
    "validate_oct_key",
]
