# Migration Portability Report

- passed: `False`
- python_version: `3.13`
- supported_backends: `sqlite, postgres`
- validated_backends: `sqlite`
- pytest_exit_code: `0`

## sqlite

- available: `True`
- passed: `True`
- upgrade_passed: `True`
- downgrade_passed: `True`
- reapply_passed: `True`
- downgraded_revision: `0007_browser_session_cookie_and_auth_code_linkage`
- artifacts:
  - `downgrade`: `dist/migration-portability/sqlite/downgrade.json`
  - `reapply`: `dist/migration-portability/sqlite/reapply.json`
  - `upgrade`: `dist/migration-portability/sqlite/upgrade.json`

## postgres

- available: `False`
- passed: `False`
- upgrade_passed: `False`
- downgrade_passed: `False`
- reapply_passed: `False`
- downgraded_revision: `None`
- failure: `POSTGRES_URL not set in the current environment.`

## open_gaps

- postgres backend was not available in the current environment.
