"""Compatibility facade for canonical RFC 7515 helpers."""

from tigrbl_auth.standards.jose.rfc7515 import RFC7515_SPEC_URL, sign_jws, verify_jws

__all__ = ["sign_jws", "verify_jws", "RFC7515_SPEC_URL"]
