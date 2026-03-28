> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.


# tigrbl_auth — exhaustive target project tree

This is the **target** tree for the new `tigrbl_auth` package, derived from:

- the revised standards/compliance matrix,
- the requirement to stay strictly Tigrbl-native,
- the requirement to adopt ADRs,
- the requirement to codify release gates,
- the current uploaded package state.

The target intentionally **removes** these current-package shapes from the certification boundary:

- `tigrbl_auth/vendor/`
- flat `tigrbl_auth/rfc/`
- flat `tigrbl_auth/routers/`
- flat runtime modules such as `backends.py`, `runtime_cfg.py`, `security.deps.py`, `db.py`

Their responsibilities are redistributed into `api/`, `tables/`, `ops/`, `services/`, `security/`, `config/`, and `standards/`.

```text
pkgs/standards/tigrbl_auth/
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .env.example
├── examples/
│   ├── standalone_app.py
│   ├── install_plugin.py
│   ├── oauth_authorization_code_pkce.py
│   ├── oauth_client_credentials.py
│   ├── oidc_rp_login.py
│   ├── device_flow.py
│   ├── token_exchange.py
│   └── service_to_service_token_exchange.py
├── scripts/
│   ├── generate_openapi.py
│   ├── generate_openrpc.py
│   ├── run_conformance.py
│   ├── validate_well_known.py
│   ├── verify_claims.py
│   ├── verify_release_gates.py
│   └── build_evidence_bundle.py
├── specs/
│   ├── openapi/
│   │   ├── openapi.yaml
│   │   ├── openapi.json
│   │   └── overlays/
│   │       ├── auth-core.yaml
│   │       ├── oidc.yaml
│   │       └── admin-control-plane.yaml
│   └── openrpc/
│       └── openrpc.json
├── docs/
│   ├── adr/
│   │   ├── README.md
│   │   ├── template.md
│   │   ├── 0001-use-adrs.md
│   │   ├── 0002-certification-boundary.md
│   │   ├── 0003-tigrbl-native-package-shape.md
│   │   ├── 0004-remove-vendor-shims.md
│   │   ├── 0005-separate-standards-from-extensions.md
│   │   ├── 0006-release-gates-as-code.md
│   │   ├── 0007-openapi-openrpc-generation.md
│   │   ├── 0008-evidence-retention-policy.md
│   │   └── 0009-peer-claim-policy.md
│   ├── standards/
│   │   ├── targets.md
│   │   ├── oauth2.md
│   │   ├── oidc.md
│   │   ├── jose.md
│   │   ├── http.md
│   │   ├── openapi.md
│   │   ├── openrpc.md
│   │   └── well_known.md
│   ├── compliance/
│   │   ├── target-matrix.md
│   │   ├── claim-tiers.md
│   │   ├── release-gates.md
│   │   ├── evidence-policy.md
│   │   ├── peer-claim-policy.md
│   │   └── threat-model.md
│   ├── runbooks/
│   │   ├── key-rotation.md
│   │   ├── incident-response.md
│   │   ├── release.md
│   │   └── interoperability.md
│   └── diagrams/
│       ├── auth-surface-context.md
│       ├── token-lifecycle.md
│       ├── browser-session-flow.md
│       └── service-to-service-flow.md
├── compliance/
│   ├── targets/
│   │   ├── rfc-targets.yaml
│   │   ├── oidc-targets.yaml
│   │   ├── openapi-targets.yaml
│   │   ├── openrpc-targets.yaml
│   │   ├── endpoint-targets.yaml
│   │   └── profiles.yaml
│   ├── gates/
│   │   ├── gate-00-structure.yaml
│   │   ├── gate-10-format-lint-types.yaml
│   │   ├── gate-20-unit.yaml
│   │   ├── gate-30-integration.yaml
│   │   ├── gate-40-conformance.yaml
│   │   ├── gate-50-interop.yaml
│   │   ├── gate-60-security.yaml
│   │   ├── gate-70-contracts.yaml
│   │   ├── gate-80-evidence.yaml
│   │   └── gate-90-release.yaml
│   ├── claims/
│   │   ├── tier-1-implemented.yaml
│   │   ├── tier-2-self-asserted.yaml
│   │   ├── tier-3-evidence-backed.yaml
│   │   └── tier-4-peer-reviewed.yaml
│   ├── evidence/
│   │   ├── internal/
│   │   │   └── README.md
│   │   ├── peer/
│   │   │   └── README.md
│   │   ├── attestations/
│   │   │   └── README.md
│   │   ├── reports/
│   │   │   └── README.md
│   │   └── sbom/
│   │       └── README.md
│   └── waivers/
│       └── README.md
├── tests/
│   ├── conftest.py
│   ├── fixtures/
│   │   ├── jwks/
│   │   │   ├── rsa_public_jwks.json
│   │   │   ├── ec_public_jwks.json
│   │   │   └── okp_public_jwks.json
│   │   ├── clients/
│   │   │   ├── public_client.json
│   │   │   ├── confidential_client.json
│   │   │   └── mtls_client.json
│   │   └── tenants/
│   │       ├── single_tenant.json
│   │       └── multi_tenant.json
│   ├── unit/
│   │   ├── test_plugin.py
│   │   ├── test_gateway.py
│   │   ├── test_settings.py
│   │   ├── test_feature_flags.py
│   │   ├── test_claim_matrix.py
│   │   ├── test_adapters.py
│   │   ├── test_tables.py
│   │   ├── test_key_management.py
│   │   ├── test_token_service.py
│   │   ├── test_session_service.py
│   │   ├── test_cookie_service.py
│   │   ├── test_nonce_service.py
│   │   ├── test_consent_service.py
│   │   ├── test_algorithm_policy.py
│   │   ├── test_session_policy.py
│   │   ├── test_security_deps.py
│   │   └── test_release_profile.py
│   ├── integration/
│   │   ├── test_rest_surface.py
│   │   ├── test_rpc_surface.py
│   │   ├── test_migrations.py
│   │   ├── test_openapi_generation.py
│   │   ├── test_openrpc_generation.py
│   │   └── test_plugin_installation.py
│   ├── conformance/
│   │   ├── oauth2/
│   │   │   ├── rfc6749/
│   │   │   │   ├── test_authorize.py
│   │   │   │   ├── test_token.py
│   │   │   │   ├── test_errors.py
│   │   │   │   └── test_grants.py
│   │   │   ├── rfc6750/
│   │   │   │   └── test_bearer_usage.py
│   │   │   ├── rfc7009/
│   │   │   │   └── test_revocation_endpoint.py
│   │   │   ├── rfc7591/
│   │   │   │   └── test_dynamic_client_registration.py
│   │   │   ├── rfc7592/
│   │   │   │   └── test_client_management.py
│   │   │   ├── rfc7636/
│   │   │   │   └── test_pkce.py
│   │   │   ├── rfc7662/
│   │   │   │   └── test_introspection.py
│   │   │   ├── rfc8252/
│   │   │   │   └── test_native_apps.py
│   │   │   ├── rfc8414/
│   │   │   │   └── test_authorization_server_metadata.py
│   │   │   ├── rfc8628/
│   │   │   │   └── test_device_authorization.py
│   │   │   ├── rfc8693/
│   │   │   │   └── test_token_exchange.py
│   │   │   ├── rfc8705/
│   │   │   │   └── test_mtls_sender_constrained_tokens.py
│   │   │   ├── rfc8707/
│   │   │   │   └── test_resource_indicators.py
│   │   │   ├── rfc9068/
│   │   │   │   └── test_jwt_access_token_profile.py
│   │   │   ├── rfc9101/
│   │   │   │   └── test_jar.py
│   │   │   ├── rfc9126/
│   │   │   │   └── test_par.py
│   │   │   ├── rfc9207/
│   │   │   │   └── test_issuer_identifier.py
│   │   │   ├── rfc9396/
│   │   │   │   └── test_rar.py
│   │   │   └── rfc9449/
│   │   │       └── test_dpop.py
│   │   ├── jose/
│   │   │   ├── rfc7515/
│   │   │   │   └── test_jws.py
│   │   │   ├── rfc7516/
│   │   │   │   └── test_jwe.py
│   │   │   ├── rfc7517/
│   │   │   │   └── test_jwk.py
│   │   │   ├── rfc7518/
│   │   │   │   └── test_jwa.py
│   │   │   ├── rfc7519/
│   │   │   │   └── test_jwt.py
│   │   │   ├── rfc7638/
│   │   │   │   └── test_jwk_thumbprint.py
│   │   │   ├── rfc7800/
│   │   │   │   └── test_proof_of_possession.py
│   │   │   ├── rfc8037/
│   │   │   │   └── test_okp_and_eddsa.py
│   │   │   └── rfc8725/
│   │   │       └── test_jwt_bcp.py
│   │   ├── oidc/
│   │   │   ├── core/
│   │   │   │   ├── test_authorize.py
│   │   │   │   ├── test_id_token.py
│   │   │   │   └── test_nonce_and_amr.py
│   │   │   ├── discovery/
│   │   │   │   ├── test_openid_configuration.py
│   │   │   │   └── test_jwks_uri.py
│   │   │   ├── session/
│   │   │   │   └── test_browser_session_management.py
│   │   │   └── logout/
│   │   │       ├── test_rp_initiated_logout.py
│   │   │       ├── test_frontchannel_logout.py
│   │   │       └── test_backchannel_logout.py
│   │   └── http/
│   │       ├── rfc5785/
│   │       │   └── test_well_known_endpoints.py
│   │       └── rfc6265/
│   │           └── test_cookie_policies.py
│   ├── interop/
│   │   ├── generic_oidc_rp/
│   │   │   ├── test_basic_login.py
│   │   │   └── test_logout.py
│   │   ├── generic_resource_server/
│   │   │   ├── test_jwt_validation.py
│   │   │   └── test_introspection_validation.py
│   │   ├── keycloak/
│   │   │   ├── test_login.py
│   │   │   └── test_token_exchange.py
│   │   ├── okta/
│   │   │   └── test_metadata_and_jwks.py
│   │   └── azure/
│   │       └── test_oidc_discovery.py
│   ├── negative/
│   │   ├── test_alg_none_rejected.py
│   │   ├── test_bad_redirect_uri_rejected.py
│   │   ├── test_pkce_verifier_mismatch.py
│   │   ├── test_replayed_nonce_rejected.py
│   │   ├── test_replayed_dpop_proof_rejected.py
│   │   ├── test_invalid_client_metadata_rejected.py
│   │   └── test_invalid_request_object_rejected.py
│   ├── e2e/
│   │   ├── test_browser_auth_code_pkce.py
│   │   ├── test_service_to_service_exchange.py
│   │   ├── test_device_flow.py
│   │   └── test_revocation_and_introspection.py
│   ├── security/
│   │   ├── test_key_rotation.py
│   │   ├── test_jwks_rollover.py
│   │   ├── test_refresh_token_rotation.py
│   │   ├── test_replay_protection.py
│   │   └── test_csrf_and_session_fixation.py
│   └── perf/
│       ├── test_token_issue_latency.py
│       └── test_introspection_throughput.py
└── tigrbl_auth/
    ├── __init__.py
    ├── plugin.py
    ├── gateway.py
    ├── api/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── lifecycle.py
    │   ├── surfaces.py
    │   ├── rest/
    │   │   ├── __init__.py
    │   │   ├── errors.py
    │   │   ├── openapi.py
    │   │   ├── deps/
    │   │   │   ├── __init__.py
    │   │   │   ├── auth.py
    │   │   │   ├── clients.py
    │   │   │   ├── tenants.py
    │   │   │   ├── sessions.py
    │   │   │   ├── security.py
    │   │   │   └── rate_limits.py
    │   │   ├── schemas/
    │   │   │   ├── __init__.py
    │   │   │   ├── common.py
    │   │   │   ├── authorize.py
    │   │   │   ├── token.py
    │   │   │   ├── registration.py
    │   │   │   ├── client_management.py
    │   │   │   ├── introspection.py
    │   │   │   ├── revocation.py
    │   │   │   ├── userinfo.py
    │   │   │   ├── logout.py
    │   │   │   ├── device.py
    │   │   │   ├── par.py
    │   │   │   ├── token_exchange.py
    │   │   │   ├── keys.py
    │   │   │   ├── metadata.py
    │   │   │   └── errors.py
    │   │   └── routers/
    │   │       ├── __init__.py
    │   │       ├── authorize.py
    │   │       ├── token.py
    │   │       ├── revocation.py
    │   │       ├── introspection.py
    │   │       ├── registration.py
    │   │       ├── client_management.py
    │   │       ├── userinfo.py
    │   │       ├── jwks.py
    │   │       ├── oauth_metadata.py
    │   │       ├── openid_configuration.py
    │   │       ├── logout.py
    │   │       ├── device_authorization.py
    │   │       ├── pushed_authorization.py
    │   │       ├── token_exchange.py
    │   │       └── health.py
    │   └── rpc/
    │       ├── __init__.py
    │       ├── openrpc.py
    │       ├── registry.py
    │       ├── schemas/
    │       │   ├── __init__.py
    │       │   ├── common.py
    │       │   ├── tenants.py
    │       │   ├── users.py
    │       │   ├── clients.py
    │       │   ├── services.py
    │       │   ├── service_keys.py
    │       │   ├── api_keys.py
    │       │   ├── sessions.py
    │       │   ├── keys.py
    │       │   ├── discovery.py
    │       │   ├── claims.py
    │       │   └── gates.py
    │       └── methods/
    │           ├── __init__.py
    │           ├── discover.py
    │           ├── tenants.py
    │           ├── users.py
    │           ├── clients.py
    │           ├── services.py
    │           ├── service_keys.py
    │           ├── api_keys.py
    │           ├── sessions.py
    │           ├── keys.py
    │           ├── claims.py
    │           └── gates.py
    ├── tables/
    │   ├── __init__.py
    │   ├── base.py
    │   ├── engine.py
    │   ├── mixins.py
    │   ├── tenant.py
    │   ├── user.py
    │   ├── client.py
    │   ├── service.py
    │   ├── service_key.py
    │   ├── api_key.py
    │   ├── auth_session.py
    │   ├── auth_code.py
    │   ├── device_code.py
    │   ├── pushed_authorization_request.py
    │   ├── revoked_token.py
    │   ├── consent.py
    │   └── audit_event.py
    ├── ops/
    │   ├── __init__.py
    │   ├── tenants.py
    │   ├── users.py
    │   ├── clients.py
    │   ├── services.py
    │   ├── service_keys.py
    │   ├── api_keys.py
    │   ├── authenticate.py
    │   ├── authorize.py
    │   ├── login.py
    │   ├── logout.py
    │   ├── consent.py
    │   ├── sessions.py
    │   ├── register_client.py
    │   ├── manage_client.py
    │   ├── issue_access_token.py
    │   ├── issue_id_token.py
    │   ├── introspect_token.py
    │   ├── revoke_token.py
    │   ├── exchange_token.py
    │   ├── device_authorization.py
    │   ├── pushed_authorization.py
    │   ├── userinfo.py
    │   └── rotate_keys.py
    ├── services/
    │   ├── __init__.py
    │   ├── key_management.py
    │   ├── jwks_service.py
    │   ├── token_service.py
    │   ├── session_service.py
    │   ├── cookie_service.py
    │   ├── nonce_service.py
    │   ├── consent_service.py
    │   ├── principal_service.py
    │   ├── audit_service.py
    │   ├── evidence_bundle.py
    │   ├── spec_generation.py
    │   └── release_gate_service.py
    ├── standards/
    │   ├── __init__.py
    │   ├── jose/
    │   │   ├── __init__.py
    │   │   ├── jws.py
    │   │   ├── jwe.py
    │   │   ├── jwk.py
    │   │   ├── jwa.py
    │   │   ├── jwt.py
    │   │   ├── thumbprint.py
    │   │   ├── proof_of_possession.py
    │   │   └── bcp8725.py
    │   ├── oauth2/
    │   │   ├── __init__.py
    │   │   ├── core.py
    │   │   ├── bearer.py
    │   │   ├── revocation.py
    │   │   ├── introspection.py
    │   │   ├── pkce.py
    │   │   ├── dynamic_registration.py
    │   │   ├── client_management.py
    │   │   ├── native_apps.py
    │   │   ├── metadata.py
    │   │   ├── jwt_access_tokens.py
    │   │   ├── jar.py
    │   │   ├── par.py
    │   │   ├── issuer_id.py
    │   │   ├── rar.py
    │   │   ├── dpop.py
    │   │   ├── mtls.py
    │   │   ├── resource_indicators.py
    │   │   ├── token_exchange.py
    │   │   ├── device_authorization.py
    │   │   └── profiles/
    │   │       ├── __init__.py
    │   │       └── oauth2_1_alignment.py
    │   ├── oidc/
    │   │   ├── __init__.py
    │   │   ├── core.py
    │   │   ├── discovery.py
    │   │   ├── id_token.py
    │   │   ├── userinfo.py
    │   │   ├── session_mgmt.py
    │   │   ├── rp_initiated_logout.py
    │   │   ├── frontchannel_logout.py
    │   │   ├── backchannel_logout.py
    │   │   └── amr.py
    │   └── http/
    │       ├── __init__.py
    │       ├── auth_framework.py
    │       ├── well_known.py
    │       ├── cookies.py
    │       └── tls.py
    ├── extensions/
    │   ├── __init__.py
    │   ├── webauthn/
    │   │   ├── __init__.py
    │   │   ├── registration.py
    │   │   ├── authentication.py
    │   │   ├── attestation.py
    │   │   ├── assertion.py
    │   │   └── metadata.py
    │   ├── webpush/
    │   │   ├── __init__.py
    │   │   └── encryption.py
    │   ├── security_event_tokens/
    │   │   ├── __init__.py
    │   │   └── set.py
    │   └── experimental/
    │       ├── __init__.py
    │       └── future_profiles.py
    ├── security/
    │   ├── __init__.py
    │   ├── deps.py
    │   ├── csrf.py
    │   ├── headers.py
    │   ├── session_policy.py
    │   ├── algorithm_policy.py
    │   ├── key_rotation.py
    │   ├── proof_of_possession.py
    │   ├── rate_limits.py
    │   ├── validators.py
    │   └── threat_model.py
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── feature_flags.py
    │   ├── claim_matrix.py
    │   ├── release_profile.py
    │   └── logging.py
    ├── adapters/
    │   ├── __init__.py
    │   ├── context.py
    │   ├── local.py
    │   ├── remote.py
    │   ├── jwks_remote.py
    │   └── subjects.py
    ├── schemas/
    │   ├── json/
    │   │   ├── openid_configuration.schema.json
    │   │   ├── authorization_server_metadata.schema.json
    │   │   ├── jwks.schema.json
    │   │   ├── client_registration.schema.json
    │   │   └── openrpc_discovery.schema.json
    │   └── examples/
    │       ├── authorization_code_token_response.json
    │       ├── openid_configuration.json
    │       └── registration_request.json
    └── migrations/
        ├── env.py
        └── versions/
            ├── 0001_initial_identity_tables.py
            ├── 0002_client_and_service_tables.py
            ├── 0003_authorization_runtime_tables.py
            ├── 0004_device_par_revocation_tables.py
            ├── 0005_session_logout_tables.py
            └── 0006_key_rotation_and_audit_tables.py
```

## Explicit replacements from current package

```text
current                                  -> target
---------------------------------------- -> --------------------------------------------
tigrbl_auth/app.py                       -> tigrbl_auth/api/app.py + tigrbl_auth/gateway.py
tigrbl_auth/backends.py                  -> tigrbl_auth/ops/authenticate.py
tigrbl_auth/crypto.py                    -> tigrbl_auth/services/key_management.py + standards/jose/*
tigrbl_auth/db.py                        -> tigrbl_auth/tables/engine.py
tigrbl_auth/security.deps.py              -> tigrbl_auth/security/deps.py + api/rest/deps/*
tigrbl_auth/jwtoken.py                   -> tigrbl_auth/standards/jose/jwt.py + services/token_service.py
tigrbl_auth/oidc_discovery.py            -> tigrbl_auth/standards/oidc/discovery.py + api/rest/routers/openid_configuration.py
tigrbl_auth/oidc_id_token.py             -> tigrbl_auth/standards/oidc/id_token.py
tigrbl_auth/oidc_userinfo.py             -> tigrbl_auth/standards/oidc/userinfo.py + ops/userinfo.py
tigrbl_auth/runtime_cfg.py               -> tigrbl_auth/config/settings.py
tigrbl_auth/principal_ctx.py             -> tigrbl_auth/adapters/context.py
tigrbl_auth/orm/*                        -> tigrbl_auth/tables/*
tigrbl_auth/routers/*                    -> tigrbl_auth/api/rest/* and tigrbl_auth/api/rpc/*
tigrbl_auth/rfc/*                        -> tigrbl_auth/standards/{oauth2,oidc,jose,http}/*
tigrbl_auth/vendor/*                     -> deleted
tests/unit/test_rfc*.py                  -> tests/conformance/<domain>/<target>/*
```
