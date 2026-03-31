# Final certification local runbook

This project certifies against the same matrix used by `.github/workflows/ci-release-gates.yml`.

## 1) Install interpreter matrix (uv)

```bash
./scripts/ci/install_uv_python_matrix.sh
```

This installs CPython 3.10, 3.11, and 3.12 via `uv python install`.

## 2) Install/start local PostgreSQL

```bash
./scripts/ci/install_local_postgres.sh
```

Defaults:
- db: `tigrbl_auth_ci`
- user/password: `postgres` / `postgres`
- host/port: `127.0.0.1:5432`

The script prints/exports `POSTGRES_URL` for workflow compatibility.

## 3) Run certification workflow jobs locally

### Clean-room matrix
```bash
tox -e py310-base,py311-base,py312-base,py310-sqlite-uvicorn,py311-sqlite-uvicorn,py312-sqlite-uvicorn,py310-postgres-hypercorn,py311-postgres-hypercorn,py312-postgres-hypercorn,py311-tigrcorn,py312-tigrcorn,py310-devtest,py311-devtest,py312-devtest
```

### Certification-lane matrix
```bash
tox -e py310-test-core,py311-test-core,py312-test-core,py310-test-integration,py311-test-integration,py312-test-integration,py310-test-conformance,py311-test-conformance,py312-test-conformance,py310-test-security-negative,py311-test-security-negative,py312-test-security-negative,py310-test-interop,py311-test-interop,py312-test-interop
```

### Migration portability + final certification
```bash
tox -e py311-migration-portability,py311-final-certification
```

## 4) Inventory generation steps

The inventory consumed by final certification is generated from validated manifests in `dist/validated-runs`.

1. Each tox environment writes a validated manifest using `scripts/record_validated_run.py`.
2. Final-certification runs `scripts/collect_validated_artifact_downloads.py` to normalize downloaded CI artifacts (if present).
3. Final-certification runs `scripts/generate_state_reports.py`, which materializes `docs/compliance/validated_execution_report.json`.
4. `scripts/run_release_gates.py` reads that inventory and enforces gate readiness (including `gate-90-release`).

Quick check:

```bash
python - <<'PY'
import json
p=json.load(open('docs/compliance/validated_execution_report.json'))
print(p['summary'])
PY
```
