"""REST auth dependency package."""

from tigrbl_auth.api.rest.deps.auth import (
    ApiKeyBackend,
    PasswordBackend,
    get_current_principal,
    get_principal,
    principal_var,
)

__all__ = [
    "ApiKeyBackend",
    "PasswordBackend",
    "get_current_principal",
    "get_principal",
    "principal_var",
]
