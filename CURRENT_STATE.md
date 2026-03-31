# CURRENT_STATE

## Summary

This repository is a **final certification aggregation checkpoint** for `tigrbl_auth`, with the retained target/profile truth reconciliation complete for RFC 7516, RFC 7592, and RFC 9207, and with the clean-room executor / validated-manifest evidence contract tightened so preserved runtime, test-lane, and migration artifacts must carry install evidence, environment identity, and backend-specific proof.

Historical planning/checkpoint material is now archived under `docs/archive/historical/` (with `docs/archive/README.md` as the archive entrypoint), and the current authoritative set is curated in the generated `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`.

The repository is **not yet certifiably fully featured**, **not yet certifiably fully RFC/spec compliant**, and **not yet certifiably fully non-RFC spec/standard compliant**.

## Current generated state

- declared in-scope claim count: `48`
- Tier 3 claim count: `48`
- Tier 4 claim count: `0`
- strict independent claims ready: `False`
- certifiably fully non-RFC spec/standard compliant now: `False`
- target/profile truth reconciled complete: `True`
- profile-scope mismatch count: `0`
- profile-scope mismatch set empty: `True`
- alignment-only checkpoint without new certification evidence: `False`
- clean-room executor matrix declared complete: `True`
- validated manifest identity contract installed: `True`
- validated runtime matrix preservation complete: `False`
- validated test-lane preservation complete: `False`
- validated migration portability preservation complete: `False`
- authoritative current doc count: `25`
- archived historical root count: `1`
- certification bundle current-state doc count: `21`
- install substrate manifest passed: `True`
- install substrate supported-python binaries detected: `3` / `3`
- install substrate current-profile import probe passed: `True`
- validated inventory present count: `30` / `30`
- validated runtime matrix passed count: `14` / `14`
- validated test-lane passed count: `15` / `15`
- migration portability passed: `True`
- runtime profile ready count: `3`
- runtime profile missing count: `0`
- runtime profile invalid count: `0`
- historical stale doc refs outside archive: `0`

## What is now claimable

- the repository has a clearly separated authoritative current documentation set
- historical / superseded planning material is preserved in a non-authoritative archive tree
- certification bundles are built from generated current-state docs only, with executable contracts copied separately as non-doc release artifacts
- the clean-room install substrate is explicitly declared in `pyproject.toml`, `constraints/*.txt`, `tox.ini`, CI workflows, and generated install-substrate reports
- the supported clean-room executor matrix is declared for Python `3.10`, `3.11`, and `3.12`, with PostgreSQL required in the preserved certification matrix rather than optional for the relevant lanes
- preserved runtime, test-lane, and migration manifests now have a stricter fail-closed evidence contract tying pass status to install evidence, environment identity, serve-check / pytest artifacts, and revision-aware backend results
- release bundles and attestations can be rebuilt and verified from the repository state
- the repository cannot yet claim a final certified release while preserved py3.10/3.11/3.12 runtime/test/migration evidence and Tier 4 external peer bundles remain incomplete

## Key artifacts to inspect

- `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`
- `docs/compliance/current_state_report.md`
- `docs/compliance/install_substrate_report.md`
- `docs/compliance/validated_execution_report.md`
- `docs/compliance/runtime_profile_report.md`
- `docs/compliance/migration_portability_report.md`
- `docs/compliance/certification_state_report.md`
- `docs/compliance/release_gate_report.md`
- `docs/compliance/final_release_gate_report.md`
- `docs/compliance/RELEASE_DECISION_RECORD.md`
- `docs/compliance/CLEAN_ROOM_EXECUTOR_AND_EVIDENCE_CHECKPOINT_2026-03-27.md`
- `docs/archive/README.md`
- `CERTIFICATION_STATUS.md`
