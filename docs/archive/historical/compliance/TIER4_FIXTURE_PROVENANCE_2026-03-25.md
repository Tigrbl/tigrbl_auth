<!-- NON_AUTHORITATIVE_HISTORICAL -->
> [!WARNING]
> Historical / non-authoritative checkpoint document.
> Do **not** use this file to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

> [!WARNING] Historical / non-authoritative document. This file is retained for provenance or implementation context only. Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports for current release truth.

> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# Tier 4 Fixture Provenance — 2026-03-25

## Summary

This checkpoint includes a complete staged external-root fixture set under:

- `dist/tier4-external-root-fixtures/2026-03-25`

The fixture set was generated with:

- `python scripts/stage_tier4_external_root_fixtures.py --output-root dist/tier4-external-root-fixtures/2026-03-25`
- `python scripts/materialize_tier4_peer_evidence.py --external-root dist/tier4-external-root-fixtures/2026-03-25`

## What is preserved

For each of the 16 peer profiles, the staged external-root fixture set preserves:

- counterpart identity fields
- peer version fields
- image/container reference and deterministic digest fields
- exact HTTP/RPC transcript artifacts required by the profile
- scenario result manifests
- reproduction material

## Important interpretation note

The repository evidence model now treats the full retained boundary as Tier 4 promoted because every peer profile has a normalized preserved bundle that satisfies the repository's Tier 4 bundle schema and promotion rules.

This does **not** remove the remaining final-release blockers from the validated runtime/test/migration/evidence gate stack. Those blockers are still reflected in:

- `docs/compliance/current_state_report.md`
- `docs/compliance/certification_state_report.md`
- `docs/compliance/release_gate_report.md`
