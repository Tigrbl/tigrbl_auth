> [!WARNING] Non-authoritative active document. For current release and certification truth, use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports.

> **Historical / non-authoritative** — This document is retained for planning, provenance, or operator guidance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# Historical Drift Cleanup Status — 2026-03-25

## Result

- active reference tree reduced to executable/current reference docs only
- historical checkpoint and superseded planning/reference docs are retained under `docs/archive/historical/`
- active current-state truth is centralized through `compliance/targets/document-authority.yaml`
- certification bundles are restricted to generated current-state docs plus supporting non-doc artifacts

## Archive policy

Historical and superseded planning/reference/checkpoint documents are non-authoritative.
Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` for the current repository truth set.

## Honest status

This cleanup removes audit friction and contradictory documentation scope, but it does **not** by itself make the repository certifiably fully featured or certifiably fully RFC compliant.