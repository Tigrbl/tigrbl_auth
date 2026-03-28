# Tier 4 External Evidence Handoff Template

This directory is a ready-to-fill handoff package for independent peers. It is **not** preserved Tier 4 evidence by itself.

- profile_count: `16`
- use `manifest.template.yaml` and `result.template.yaml` as fill-in templates
- each manifest now requires peer operator identity plus explicit attesting organization/contact/timestamp metadata
- repository-staged fixtures under `dist/tier4-external-root-fixtures/` are intentionally non-qualifying and are rejected for Tier 4 promotion
- replace placeholder artifacts with externally generated preserved artifacts before materialization
- review `VALIDATION_RULES.md` before submission
- normalize with `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root> --require-full-boundary`

## Profiles

- `assertion-client` -> `assertion-client-harness` -> `RFC 7515, RFC 7517, RFC 7518, RFC 7519, RFC 7521, RFC 7523, RFC 7009`
- `browser` -> `browser-rp` -> `RFC 6749, RFC 7636, RFC 7516, RFC 8414, RFC 8615, RFC 9207, OIDC Core 1.0, OIDC Discovery 1.0, OIDC UserInfo`
- `client-mgmt` -> `client-mgmt-harness` -> `RFC 7591, RFC 7592`
- `device` -> `device-client` -> `RFC 8628`
- `dpop` -> `dpop-client` -> `RFC 9449, RFC 9700`
- `gateway` -> `gateway-peer` -> `RFC 6750, RFC 8414, RFC 8615, RFC 7517, RFC 9700, RFC 9728, OIDC Discovery 1.0`
- `mtls` -> `mtls-peer` -> `RFC 8705, RFC 9700`
- `native` -> `native-client` -> `RFC 7636, RFC 8252, RFC 7516, RFC 9207`
- `ops-cli` -> `ops-cli-harness` -> `OpenAPI 3.1 / 3.2 compatible public contract, OpenRPC 1.4.x admin/control-plane contract, CLI operator surface, Bootstrap and migration lifecycle, Key lifecycle and JWKS publication, Import/export portability, Release bundle and signature verification`
- `par-jar-rar` -> `par-jar-rar-client` -> `RFC 9101, RFC 9126, RFC 9396, RFC 8707`
- `resource-server` -> `resource-server` -> `RFC 6750, RFC 7662, RFC 8693, RFC 8707, RFC 9068, RFC 9728, RFC 9700`
- `rp-session-logout` -> `rp-session-logout-rp` -> `RFC 6265, OIDC Session Management, OIDC RP-Initiated Logout, OIDC Front-Channel Logout, OIDC Back-Channel Logout`
- `runner-hypercorn` -> `hypercorn-runner` -> `ASGI 3 application package, Runner profile: Hypercorn`
- `runner-tigrcorn` -> `tigrcorn-runner` -> `ASGI 3 application package, Runner profile: Tigrcorn`
- `runner-uvicorn` -> `uvicorn-runner` -> `ASGI 3 application package, Runner profile: Uvicorn`
- `spa` -> `spa-rp` -> `RFC 6749, RFC 7636, OIDC Core 1.0, OIDC Discovery 1.0`
