<!-- NON_AUTHORITATIVE_HISTORICAL -->
> [!WARNING]
> Historical / non-authoritative checkpoint document.
> Do **not** use this file to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# OpenRPC Contract Summary

- Title: `tigrbl_auth admin/control-plane`
- Version: `0.3.2.dev14`
- Profile: `baseline`
- Method count: `35`
- Schema count: `68`

## Methods

- `audit.export` — Export durable audit events. (`tigrbl_auth/api/rpc/methods/audit.py`)
- `audit.list` — List durable audit events. (`tigrbl_auth/api/rpc/methods/audit.py`)
- `claims.lint` — Run claims lint against the governance plane. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `claims.show` — Return effective claims for the active deployment profile. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `client.list` — List OAuth/OIDC clients in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `client.registration.delete` — Delete a durable client-registration record. (`tigrbl_auth/api/rpc/methods/client_registration.py`)
- `client.registration.list` — List durable client-registration records. (`tigrbl_auth/api/rpc/methods/client_registration.py`)
- `client.registration.show` — Show a durable client-registration record. (`tigrbl_auth/api/rpc/methods/client_registration.py`)
- `client.registration.upsert` — Create or update a durable client-registration record. (`tigrbl_auth/api/rpc/methods/client_registration.py`)
- `client.show` — Show a client in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `consent.list` — List durable consent records. (`tigrbl_auth/api/rpc/methods/consent.py`)
- `consent.revoke` — Revoke a durable consent record. (`tigrbl_auth/api/rpc/methods/consent.py`)
- `consent.show` — Show a durable consent record. (`tigrbl_auth/api/rpc/methods/consent.py`)
- `discovery.show` — Show effective OIDC discovery metadata for the deployment. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `evidence.status` — Summarize evidence-plane status. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `flow.list` — List effective protocol flow slices for the current deployment. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `gate.run` — Run a named release gate. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `identity.list` — List identities in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `identity.show` — Show an identity in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `jwks.show` — Show the effective JWKS document. (`tigrbl_auth/api/rpc/methods/keys.py`)
- `keys.list` — List durable service keys and key-rotation history. (`tigrbl_auth/api/rpc/methods/keys.py`)
- `keys.rotate` — Rotate the signing key and persist a key-rotation event. (`tigrbl_auth/api/rpc/methods/keys.py`)
- `profile.show` — Show the effective deployment/profile posture. (`tigrbl_auth/api/rpc/methods/profile.py`)
- `release.bundle` — Build a release bundle. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `rpc.discover` — Return the active implementation-backed RPC method catalog. (`tigrbl_auth/api/rpc/methods/governance.py`)
- `session.list` — List durable browser and auth sessions. (`tigrbl_auth/api/rpc/methods/session.py`)
- `session.show` — Show a durable session and its latest logout state. (`tigrbl_auth/api/rpc/methods/session.py`)
- `session.terminate` — Terminate a durable session and persist logout state. (`tigrbl_auth/api/rpc/methods/session.py`)
- `target.list` — List certification-scope targets. (`tigrbl_auth/api/rpc/methods/profile.py`)
- `target.show` — Show a certification-scope target. (`tigrbl_auth/api/rpc/methods/profile.py`)
- `tenant.list` — List tenants in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `tenant.show` — Show a tenant in the admin plane. (`tigrbl_auth/api/rpc/methods/directory.py`)
- `token.exchange` — Create a durable token exchange record. (`tigrbl_auth/api/rpc/methods/token.py`)
- `token.inspect` — Inspect token posture and current introspection state. (`tigrbl_auth/api/rpc/methods/token.py`)
- `token.list` — List durable token records. (`tigrbl_auth/api/rpc/methods/token.py`)
