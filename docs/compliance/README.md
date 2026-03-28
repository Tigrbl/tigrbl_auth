# Compliance Reports

This directory contains the current generated certification-state artifacts plus a smaller set of retained supporting reports.

## Current authoritative docs

Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.json` to determine which documents are authoritative for the current checkpoint.

Inspect `docs/compliance/install_substrate_report.{json,md}` together with `runtime_profile_report.{json,md}` when evaluating clean-room install readiness versus executable runtime readiness.

The repository-root `CURRENT_STATE.md` and `CERTIFICATION_STATUS.md`, plus the generated state and gate reports listed in the authority manifest, are the only current sources for release-readiness decisions.

The current checkpoint also includes an alignment-only target/profile truth reconciliation for `RFC 7516`, `RFC 7592`, and `RFC 9207`. No new certification evidence was collected as part of that normalization step; remaining blockers are still the validated runtime/test/migration/Tier 4 gates.

## Historical / non-authoritative docs

Historical and superseded planning/checkpoint material is retained under `docs/archive/`.

Any file in `docs/compliance/` that is not listed in `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` should be treated as non-authoritative supporting material unless a generated current-state report links to it explicitly.

## Certification bundle policy

Only the generated current-state documentation listed under `current_release_bundle_docs` in `compliance/targets/document-authority.yaml` is copied into certification release bundles. Historical docs, scaffold notes, and superseded planning material are excluded from the bundle documentation scope.

For a concise change log of this normalization-only update, see `docs/compliance/TARGET_PROFILE_TRUTH_RECONCILIATION_CHANGESET_2026-03-27.md`.
