"""Executable migration runner and schema verification helpers."""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from tigrbl_auth.migrations.helpers import applied_revisions, column_names, mark_revision, table_names, unmark_revision
from tigrbl_auth.runtime.engine_resolver import resolve_api_provider
from tigrbl_auth.tables import Base
from tigrbl_auth.tables.engine import ENGINE

VERSIONS_DIR = Path(__file__).resolve().parent / "versions"


@dataclass(slots=True)
class MigrationResult:
    applied: list[str]
    pending_before: list[str]
    expected_tables: list[str]
    actual_tables: list[str]
    missing_tables: list[str]
    passed: bool


@dataclass(slots=True)
class SchemaVerification:
    passed: bool
    expected_tables: list[str]
    actual_tables: list[str]
    missing_tables: list[str]
    unexpected_tables: list[str]


def _resolve_provider():
    try:
        from tigrbl_auth.api.surfaces import surface_api

        provider = resolve_api_provider(surface_api)
        if provider is not None:
            return provider
    except Exception:
        pass
    return ENGINE.provider


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load migration module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def iter_migration_modules() -> list[Any]:
    return [_load_module(path) for path in sorted(VERSIONS_DIR.glob("*.py")) if path.name != "__init__.py"]


def expected_table_names() -> list[str]:
    names: list[str] = []
    for table in sorted(Base.metadata.sorted_tables, key=lambda item: item.name):
        if table.schema == "authn":
            names.append(table.name)
    return names


def verify_schema_sync(conn) -> SchemaVerification:
    expected = expected_table_names()
    actual = sorted(table_names(conn))
    expected_set = set(expected)
    actual_set = set(actual)
    missing = sorted(expected_set - actual_set)
    unexpected = sorted(actual_set - expected_set - {"schema_migrations"})
    return SchemaVerification(
        passed=not missing,
        expected_tables=expected,
        actual_tables=actual,
        missing_tables=missing,
        unexpected_tables=unexpected,
    )


def column_names_sync(conn, table: str) -> list[str]:
    return sorted(column_names(conn, table))


async def apply_all_async() -> MigrationResult:
    provider = _resolve_provider()
    raw_engine, _ = provider.ensure()

    def _upgrade(sync_conn):
        modules = iter_migration_modules()
        pending_before = [module.revision for module in modules if module.revision not in applied_revisions(sync_conn)]
        applied_now: list[str] = []
        for module in modules:
            if module.revision in applied_revisions(sync_conn):
                continue
            module.upgrade(sync_conn)
            mark_revision(sync_conn, module.revision)
            applied_now.append(module.revision)
        verification = verify_schema_sync(sync_conn)
        return MigrationResult(
            applied=applied_now,
            pending_before=pending_before,
            expected_tables=verification.expected_tables,
            actual_tables=verification.actual_tables,
            missing_tables=verification.missing_tables,
            passed=verification.passed,
        )

    async with raw_engine.begin() as conn:
        return await conn.run_sync(_upgrade)


async def downgrade_one_async() -> str | None:
    provider = _resolve_provider()
    raw_engine, _ = provider.ensure()

    def _downgrade(sync_conn):
        modules = iter_migration_modules()
        applied = applied_revisions(sync_conn)
        for module in reversed(modules):
            if module.revision in applied:
                module.downgrade(sync_conn)
                unmark_revision(sync_conn, module.revision)
                return module.revision
        return None

    async with raw_engine.begin() as conn:
        return await conn.run_sync(_downgrade)


async def verify_schema_async() -> SchemaVerification:
    provider = _resolve_provider()
    raw_engine, _ = provider.ensure()
    async with raw_engine.begin() as conn:
        return await conn.run_sync(verify_schema_sync)


async def column_names_async(table: str) -> list[str]:
    provider = _resolve_provider()
    raw_engine, _ = provider.ensure()
    async with raw_engine.begin() as conn:
        return await conn.run_sync(lambda sync_conn: column_names_sync(sync_conn, table))


__all__ = [
    "MigrationResult",
    "SchemaVerification",
    "apply_all_async",
    "column_names_async",
    "column_names_sync",
    "downgrade_one_async",
    "expected_table_names",
    "iter_migration_modules",
    "verify_schema_async",
    "verify_schema_sync",
]
