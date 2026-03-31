# Validated Artifact Collection Process — 2026-03-31

This note documents the repeatable process used to rebuild a complete validated artifact matrix and re-run final release gates.

## Root cause discovered

`record_validated_run.py` preferred profile-level install substrate artifacts (`dist/install-substrate/<profile>.json`) before tox-env scoped artifacts (`dist/install-substrate/<tox_env>.json`).

For multi-Python certification evidence, that causes manifests for `py3.10` / `py3.11` / `py3.12` to bind to the wrong environment identity and fail `install_evidence_ready`.

## Fix applied

Updated candidate precedence in `scripts/record_validated_run.py` so tox-env artifacts are selected first:

1. `dist/install-substrate/<tox_env>.json`
2. `dist/install-substrate/<profile>.json`
3. `docs/compliance/install_substrate_report.json`

## Artifact collection / regeneration workflow

1. Generate or normalize runtime smoke and serve-check artifacts under `dist/runtime-smoke/`.
2. Ensure tox-env install substrate artifacts are available under `dist/install-substrate/py<ver>-*.json`.
3. Generate validated runtime manifests for each kept runtime matrix cell:
   - `base`: py3.10/py3.11/py3.12
   - `sqlite-uvicorn`: py3.10/py3.11/py3.12
   - `postgres-hypercorn`: py3.10/py3.11/py3.12
   - `tigrcorn`: py3.11/py3.12
   - `devtest`: py3.10/py3.11/py3.12
4. Generate validated test-lane manifests for each in-scope lane at py3.10/py3.11/py3.12:
   - `core`, `integration`, `conformance`, `security-negative`, `interop`
5. Generate a validated migration portability manifest (`migration-portability-py311.json`) with both sqlite + postgres pass evidence.
6. Rebuild tier-3 evidence linkage (`python scripts/record_validated_run.py tier3-evidence`).
7. Regenerate state reports (`python scripts/generate_state_reports.py`).
8. Run release gates (`python scripts/run_release_gates.py`) and confirm all 20 gates pass.

## Exit criteria verified

- `validated_inventory_present_count = 30`
- `validated_inventory_complete = true`
- `clean_room_install_matrix_green = true`
- `in_scope_test_lanes_green = true`
- `migration_portability_passed = true`
- `gate-20-tests = pass`
- `gate-90-release = pass`
- final release gates report passes with `failed_gate_count = 0`
