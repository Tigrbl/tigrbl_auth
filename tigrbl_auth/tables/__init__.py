"""Persistence models and engine exports for the Tigrbl-native package tree."""

from tigrbl_auth.framework import Base
from tigrbl_auth.config.settings import settings

from .tenant import Tenant
from .user import User
from .client import Client, _CLIENT_ID_RE
from .client_registration import ClientRegistration
from .service import Service
from .api_key import ApiKey
from .service_key import ServiceKey
from .auth_session import AuthSession
from .auth_code import AuthCode
from .device_code import DeviceCode
from .revoked_token import RevokedToken
from .token_record import TokenRecord
from .pushed_authorization_request import PushedAuthorizationRequest
from .consent import Consent
from .audit_event import AuditEvent
from .logout_state import LogoutState
from .key_rotation_event import KeyRotationEvent
from .engine import ENGINE, dsn, get_db

__all__ = [
    "Base",
    "settings",
    "ENGINE",
    "dsn",
    "get_db",
    "Tenant",
    "User",
    "Client",
    "_CLIENT_ID_RE",
    "ClientRegistration",
    "Service",
    "ApiKey",
    "ServiceKey",
    "AuthSession",
    "AuthCode",
    "DeviceCode",
    "RevokedToken",
    "TokenRecord",
    "PushedAuthorizationRequest",
    "Consent",
    "AuditEvent",
    "LogoutState",
    "KeyRotationEvent",
]
