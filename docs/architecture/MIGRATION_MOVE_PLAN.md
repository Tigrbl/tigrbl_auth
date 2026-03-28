> [!WARNING] Non-authoritative active document. For current release and certification truth, use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports.

<!-- NON_AUTHORITATIVE_HISTORICAL -->
> [!WARNING]
> Historical / non-authoritative checkpoint document.
> Do **not** use this file to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

> [!WARNING] Historical / non-authoritative document. This file is retained for provenance or implementation context only. Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports for current release truth.

> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# Migration Move Plan

## Direct move map

- `tigrbl_auth/app.py` → `tigrbl_auth/api/app.py`
- `tigrbl_auth/routers/surface.py` → `tigrbl_auth/api/surfaces.py`
- `tigrbl_auth/routers/auth_flows.py` → `tigrbl_auth/api/rest/routers/login.py`
- `tigrbl_auth/routers/authz/oidc.py` → `tigrbl_auth/api/rest/routers/authorize.py`
- `tigrbl_auth/orm/*` → `tigrbl_auth/tables/*`
- `tigrbl_auth/db.py` → `tigrbl_auth/tables/engine.py`
- `tigrbl_auth/runtime_cfg.py` → `tigrbl_auth/config/settings.py`
- `tigrbl_auth/backends.py` → `tigrbl_auth/services/auth_backends.py` and `tigrbl_auth/ops/authenticate.py`
- `tigrbl_auth/crypto.py` + `tigrbl_auth/jwtoken.py` → `tigrbl_auth/services/key_management.py` + `tigrbl_auth/services/token_service.py`
- `tigrbl_auth/oidc_discovery.py` / `tigrbl_auth/oidc_id_token.py` / `tigrbl_auth/oidc_userinfo.py` → `tigrbl_auth/standards/oidc/*`
- `tigrbl_auth/rfc/*` → `tigrbl_auth/standards/{oauth2,oidc,jose,http}/*`
- `vendor/*` → deleted / forbidden
- `tests/integration/*` → `tests/integration/*`

## Replacement order

1. framework and config
2. plugin, gateway, api app/lifecycle/surfaces
3. tables and migrations
4. services and ops
5. standards/jose
6. baseline standards/oauth2
7. baseline standards/oidc
8. api/rest routers
9. security
10. production targets
11. hardening targets
12. CLI, contracts, evidence, release automation
