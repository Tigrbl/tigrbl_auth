# Validated Artifact Collection Process

## Purpose

This runbook describes how to materialize and preserve the validated certification artifact matrix under `dist/validated-runs/` so release gates can be evaluated from preserved evidence.

## Matrix requirements

The release gates require all of the following preserved manifests:

- Runtime profile matrix: `14` cells (`base`, `sqlite-uvicorn`, `postgres-hypercorn`, `tigrcorn`, `devtest` across supported Python versions).
- Test lane matrix: `15` cells (`core`, `integration`, `conformance`, `security-negative`, `interop` across supported Python versions).
- Migration portability: `1` manifest proving both `sqlite` and `postgres` portability checks.

Total required validated inventory: `30` manifests.

## Collection workflow

1. Download artifacts from clean-room CI runs (or equivalent executor pool) into a local collection root.
2. Normalize downloaded artifacts into repository layout:
   - `dist/validated-runs/*.json`
   - `dist/migration-portability/**`
3. Reconcile and index the collected manifests:

```bash
python scripts/collect_validated_artifact_downloads.py --artifacts-root <download_root>
```

4. Rebuild reporting from the preserved manifests:

```bash
python scripts/generate_state_reports.py
```

5. Recompute Tier 3 rebuild evidence manifest:

```bash
python scripts/record_validated_run.py tier3-evidence
```

6. Re-run release gates:

```bash
python scripts/run_release_gates.py
```

## Acceptance checks

A successful collection should satisfy all of the following in `docs/compliance/validated_execution_report.json` and `docs/compliance/release_gate_report.json`:

- `validated_inventory_complete: true`
- `runtime_matrix_green: true`
- `in_scope_test_lanes_green: true`
- `migration_portability_passed: true`

## Notes

- The validated matrix is evaluated from preserved manifests, not ad-hoc local probing.
- Keep `dist/validated-runs/collected-artifact-downloads.json` updated alongside matrix manifests.
