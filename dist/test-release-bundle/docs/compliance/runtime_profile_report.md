# Runtime Profile Report

- Generated at: `20260326T212743Z`
- Deployment profile: `baseline`
- Application factory probe passed: `False`
- Ready profiles: `0`
- Missing profiles: `1`
- Invalid profiles: `2`
- Application hash invariant: `True`
- Pyproject requires-python: `>=3.10,<3.13`
- Supported Python versions: `3.10, 3.11, 3.12`
- Placeholder-supported runners: `0`
- Declared CI-installable runners: `3`
- Declared CI install/probe complete: `True`
- Execution probes enabled: `False`
- Surface probe passed: `False`
- Surface probe endpoints: `0`
- Serve-check passes: `0`
- Execution probe complete: `False`

## Application probe

- Factory: `tigrbl_auth.api.app.build_app`
- Message: `No module named 'tigrbl'`

## Runtime HTTP surface probe

- Executed: `False`
- Passed: `False`
- Message: `Skipped because the application factory did not materialize in this environment.`
- Endpoint count: `0`
- Passed count: `0`
- Failed count: `0`

## Profiles

### `hypercorn`

- Status: `invalid`
- Installed: `True`
- Available module: `hypercorn`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `c77fd754cbf6743178d8cc51a004988e1c3f146dda9d6b6adf8a33c570dde01e`
- Placeholder-supported: `False`
- Declared installable from repository: `True`
- Supported Python versions: `3.10, 3.11, 3.12`
- Tox envs: `py310-postgres-hypercorn, py311-postgres-hypercorn, py312-postgres-hypercorn`
- CI install job present: `True`
- Release-gate probe present: `True`
- Serve-check executed: `False`
- Serve-check passed: `False`
- Serve-check command: `tigrbl-auth serve --repo-root /mnt/data/step9/tigrbl_auth_phase13_certification_target_freeze_reconciled_2026-03-24 --server hypercorn --format json --check`
- Serve-check message: `Execution probes were disabled for this invocation.`
- Serve-check exit code: `None`
- Diagnostics: none

### `tigrcorn`

- Status: `missing`
- Installed: `False`
- Available module: `None`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `e5c4b6c30a0963fc4d19266bca81a908e98e52ab26fd6f7905b42ab8871f3a90`
- Placeholder-supported: `False`
- Declared installable from repository: `True`
- Supported Python versions: `3.11, 3.12`
- Tox envs: `py311-tigrcorn, py312-tigrcorn`
- CI install job present: `True`
- Release-gate probe present: `True`
- Serve-check executed: `False`
- Serve-check passed: `False`
- Serve-check command: `tigrbl-auth serve --repo-root /mnt/data/step9/tigrbl_auth_phase13_certification_target_freeze_reconciled_2026-03-24 --server tigrcorn --format json --check`
- Serve-check message: `Execution probes were disabled for this invocation.`
- Serve-check exit code: `None`
- Diagnostics:
  - `warning` `runner-not-installed` — Runner adapter is declared but the backing server package is not installed in this environment.

### `uvicorn`

- Status: `invalid`
- Installed: `True`
- Available module: `uvicorn`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `daeb45c2834409d61b8a3c58d8289a003f4d0c14ab5c5335911338217e9c4029`
- Placeholder-supported: `False`
- Declared installable from repository: `True`
- Supported Python versions: `3.10, 3.11, 3.12`
- Tox envs: `py310-sqlite-uvicorn, py311-sqlite-uvicorn, py312-sqlite-uvicorn`
- CI install job present: `True`
- Release-gate probe present: `True`
- Serve-check executed: `False`
- Serve-check passed: `False`
- Serve-check command: `tigrbl-auth serve --repo-root /mnt/data/step9/tigrbl_auth_phase13_certification_target_freeze_reconciled_2026-03-24 --server uvicorn --format json --check`
- Serve-check message: `Execution probes were disabled for this invocation.`
- Serve-check exit code: `None`
- Diagnostics: none
