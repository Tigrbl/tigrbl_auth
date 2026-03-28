<!-- NON_AUTHORITATIVE_HISTORICAL -->

> [!WARNING]
> Historical checkpoint / planning note — non-authoritative for the current release.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` for current release truth.

> [!WARNING] Historical / non-authoritative document. This file is retained for provenance or implementation context only. Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports for current release truth.

> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# Test Graph Green Status — 2026-03-24

## What changed in this checkpoint

- fixed the explicit pytest dependency conflict between `pytest==8.0.0` and `pytest-asyncio==0.24.0` by moving the test-tooling pin to `pytest==8.4.1`
- added dependency-aware test collection in `tests/conftest.py` and `tests/lanes.py`
- repaired the integration harness bug in `tests/integration/test_full_workflow.py` (`import conftest` -> package-qualified import)
- split the suite into certification lanes: `core`, `integration`, `conformance`, `security-negative`, `interop`, and `extension`
- isolated deferred or extension RFC tests (for example `RFC 7800`, `RFC 7952`, `RFC 8291`, `RFC 8812`, and `RFC 8932`) from the default core certification lane
- defined tox and CI lane jobs across supported interpreters `3.10`, `3.11`, and `3.12`

## Current-container evidence

- zero collection errors: `True`
- default core lane result: `59 passed, 7 skipped`
- collect-only counts:
  - core: `66`
  - integration: `31`
  - conformance: `22`
  - security-negative: `1`
  - interop: `11`
  - extension: `15`
  - all lanes combined: `146`

## Remaining truthful gap

This checkpoint makes the test graph **collection-clean** and **lane-separated** in the current container, but it does **not** prove that every in-scope lane has executed successfully across the supported Python 3.10–3.12 interpreter matrix. That preserved supported-interpreter execution evidence is still required before the package can be honestly called certifiably fully featured or certifiably fully RFC compliant.
