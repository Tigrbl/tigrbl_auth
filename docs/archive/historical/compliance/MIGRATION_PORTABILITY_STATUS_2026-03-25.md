<!-- NON_AUTHORITATIVE_HISTORICAL -->

> [!WARNING]
> Historical checkpoint / planning note — non-authoritative for the current release.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` for current release truth.

> [!WARNING] Historical / non-authoritative document. This file is retained for provenance or implementation context only. Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports for current release truth.

> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# Migration Portability Status — 2026-03-25

## What changed

- revision `0007_browser_session_cookie_and_auth_code_linkage` now has an implemented downgrade path
- SQLite downgrade uses a portable drop-column strategy with rebuild fallback
- PostgreSQL downgrade drops the added columns directly
- migration runtime helpers now expose column-level verification helpers
- integration coverage now checks upgrade → downgrade → reapply semantics for the `sessions` and `auth_codes` columns added by `0007`

## Truthful status in this checkpoint

- rollback policy is now explicit in `docs/runbooks/MIGRATION_AND_ROLLFORWARD.md`
- code and tests now model SQLite + PostgreSQL downgrade portability for `0007`
- preserved validated execution evidence for both backends is still absent in this checkpoint
