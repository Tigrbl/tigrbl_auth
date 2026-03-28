# Runtime Profile Report

- Generated at: `20260324T070429Z`
- Deployment profile: `baseline`
- Application factory probe passed: `False`
- Ready profiles: `0`
- Missing profiles: `1`
- Invalid profiles: `2`
- Application hash invariant: `True`

## Application probe

- Factory: `tigrbl_auth.api.app.build_app`
- Message: `No module named 'tigrbl'`

## Profiles

### `hypercorn`

- Status: `invalid`
- Installed: `True`
- Available module: `hypercorn`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `c77fd754cbf6743178d8cc51a004988e1c3f146dda9d6b6adf8a33c570dde01e`
- Diagnostics: none

### `tigrcorn`

- Status: `missing`
- Installed: `False`
- Available module: `None`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `e5c4b6c30a0963fc4d19266bca81a908e98e52ab26fd6f7905b42ab8871f3a90`
- Diagnostics:
  - `warning` `runner-not-installed` — Runner adapter is declared but the backing server package is not installed in this environment.

### `uvicorn`

- Status: `invalid`
- Installed: `True`
- Available module: `uvicorn`
- Application hash: `6bc1a1a15b32c0648a59427ad5d2e68761cd5f5d7ae89bef383842e1dc579b43`
- Runtime hash: `daeb45c2834409d61b8a3c58d8289a003f4d0c14ab5c5335911338217e9c4029`
- Diagnostics: none
