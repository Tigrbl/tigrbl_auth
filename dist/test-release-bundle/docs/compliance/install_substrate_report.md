# Install Substrate Report

- Generated at: `20260326T212728Z`
- Passed: `False`
- Static manifest passed: `True`
- Profile: `base`
- Current Python: `3.13.5`
- Current Python supported: `False`
- Expected supported Python versions: `3.10, 3.11, 3.12`
- Detected supported Python binaries: `0` / `3`
- Certification tox envs declared: `33`
- Runtime matrix envs declared: `14`
- Test lane envs declared: `15`
- Tox templates with pip check: `14` / `14`
- Tox templates with install probe: `14` / `14`
- Current profile import probe passed: `False`
- Runtime surface probe passed: `True`

## Failures

- The current environment is outside the declared certification interpreter support range.
- The current environment does not provide the full supported interpreter matrix required for clean-room certification.
- The current environment is missing one or more modules required by the selected install profile.

## Warnings

- Current container Python is outside the declared certification support range (>=3.10,<3.13).
- The current container does not provide supported interpreter binaries for: 3.10, 3.11, 3.12.

## Current environment import probe

- `tigrbl` (tigrbl) → passed=`False` message=`No module named 'tigrbl'`
- `swarmauri_core` (swarmauri_core) → passed=`False` message=`No module named 'swarmauri_core'`
- `swarmauri_base` (swarmauri_base) → passed=`False` message=`No module named 'swarmauri_base'`
- `swarmauri_standard` (swarmauri_standard) → passed=`False` message=`No module named 'swarmauri_standard'`
- `swarmauri_tokens_jwt` (swarmauri_tokens_jwt) → passed=`False` message=`No module named 'swarmauri_tokens_jwt'`
- `swarmauri_signing_jws` (swarmauri_signing_jws) → passed=`False` message=`No module named 'swarmauri_signing_jws'`
- `swarmauri_signing_ed25519` (swarmauri_signing_ed25519) → passed=`False` message=`No module named 'swarmauri_signing_ed25519'`
- `swarmauri_signing_dpop` (swarmauri_signing_dpop) → passed=`False` message=`No module named 'swarmauri_signing_dpop'`
- `swarmauri_crypto_jwe` (swarmauri_crypto_jwe) → passed=`False` message=`No module named 'swarmauri_crypto_jwe'`
- `swarmauri_crypto_paramiko` (swarmauri_crypto_paramiko) → passed=`False` message=`No module named 'swarmauri_crypto_paramiko'`
- `swarmauri_keyprovider_file` (swarmauri_keyprovider_file) → passed=`False` message=`No module named 'swarmauri_keyprovider_file'`
- `swarmauri_keyprovider_local` (swarmauri_keyprovider_local) → passed=`False` message=`No module named 'swarmauri_keyprovider_local'`
- `sqlalchemy` (sqlalchemy) → passed=`False` message=`No module named 'sqlalchemy'`
- `bcrypt` (bcrypt) → passed=`False` message=`No module named 'bcrypt'`
- `httpx` (httpx) → passed=`True` message=`import ok`
- `yaml` (PyYAML) → passed=`True` message=`import ok`
- `pydantic` (pydantic) → passed=`True` message=`import ok`
- `pydantic_settings` (pydantic-settings) → passed=`True` message=`import ok`
- `dotenv` (python-dotenv) → passed=`True` message=`import ok`
- `multipart` (python-multipart) → passed=`True` message=`import ok`
- `aiosqlite` (aiosqlite) → passed=`False` message=`No module named 'aiosqlite'`

## Runtime import surfaces

- `tigrbl_auth.api.app` → passed=`True` message=`import surface resolvable`
- `tigrbl_auth.app` → passed=`True` message=`import surface resolvable`
- `tigrbl_auth.plugin` → passed=`True` message=`import surface resolvable`
- `tigrbl_auth.gateway` → passed=`True` message=`import surface resolvable`

## Detected supported interpreters

- `3.10` → available=`False` path=`None`
- `3.11` → available=`False` path=`None`
- `3.12` → available=`False` path=`None`

## Workflow coverage

- install_profiles_workflow_present: `True`
- release_gates_workflow_present: `True`
- install_profiles_runtime_env_present_count: `14`
- release_gates_runtime_env_present_count: `14`
- release_gates_test_lane_env_present_count: `15`
- release_gates_extra_env_present_count: `2`
- install_profiles_artifact_upload_present: `True`
- release_gates_artifact_upload_present: `True`
