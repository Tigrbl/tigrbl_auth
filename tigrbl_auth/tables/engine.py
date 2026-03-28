"""Tigrbl-native engine and DB dependency wiring."""

from tigrbl_auth.framework import build_engine
from tigrbl_auth.config.settings import settings

if settings.pg_dsn_env or (settings.pg_host and settings.pg_db and settings.pg_user):
    dsn = settings.apg_dsn
else:
    dsn = "sqlite+aiosqlite:///./authn.db"

ENGINE = build_engine(dsn)
get_db = ENGINE.get_db

__all__ = ["ENGINE", "dsn", "get_db"]
