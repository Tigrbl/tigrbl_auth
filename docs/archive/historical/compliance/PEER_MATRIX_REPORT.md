# Peer Matrix Report

## Summary

- profile_count: `16`
- candidate_profile_count: `16`
- external_bundle_count: `0`
- promoted_target_count: `0`
- retained_target_count: `48`
- tier4_claims_present: `False`
- retained_boundary_promoted: `False`
- supported_peer_profile_count: `16`
- required_external_bundle_count: `16`
- valid_external_bundle_count: `0`
- invalid_external_bundle_count: `0`
- missing_external_bundle_count: `16`
- profiles_missing_external_bundles: `['assertion-client', 'browser', 'client-mgmt', 'device', 'dpop', 'gateway', 'mtls', 'native', 'ops-cli', 'par-jar-rar', 'resource-server', 'rp-session-logout', 'runner-hypercorn', 'runner-tigrcorn', 'runner-uvicorn', 'spa']`
- profiles_with_invalid_external_bundles: `[]`
- strict_independent_claims_ready: `False`

## Profiles

| Profile | Counterpart | Runtime | Targets | Candidate | External bundle | Tier 4 promotable targets | Validation failures |
|---|---|---|---|---|---|---|---|
| assertion-client | assertion-client-harness | production | RFC 7515, RFC 7517, RFC 7518, RFC 7519, RFC 7521, RFC 7523, RFC 7009 | compliance/evidence/tier4/candidates/assertion-client |  | — | — |
| browser | browser-rp | hardening | RFC 6749, RFC 7636, RFC 7516, RFC 8414, RFC 8615, RFC 9207, OIDC Core 1.0, OIDC Discovery 1.0, OIDC UserInfo | compliance/evidence/tier4/candidates/browser |  | — | — |
| client-mgmt | client-mgmt-harness | hardening | RFC 7591, RFC 7592 | compliance/evidence/tier4/candidates/client-mgmt |  | — | — |
| device | device-client | hardening | RFC 8628 | compliance/evidence/tier4/candidates/device |  | — | — |
| dpop | dpop-client | hardening | RFC 9449, RFC 9700 | compliance/evidence/tier4/candidates/dpop |  | — | — |
| gateway | gateway-peer | hardening | RFC 6750, RFC 8414, RFC 8615, RFC 7517, RFC 9700, RFC 9728, OIDC Discovery 1.0 | compliance/evidence/tier4/candidates/gateway |  | — | — |
| mtls | mtls-peer | hardening | RFC 8705, RFC 9700 | compliance/evidence/tier4/candidates/mtls |  | — | — |
| native | native-client | hardening | RFC 7636, RFC 8252, RFC 7516, RFC 9207 | compliance/evidence/tier4/candidates/native |  | — | — |
| ops-cli | ops-cli-harness | production | OpenAPI 3.1 / 3.2 compatible public contract, OpenRPC 1.4.x admin/control-plane contract, CLI operator surface, Bootstrap and migration lifecycle, Key lifecycle and JWKS publication, Import/export portability, Release bundle and signature verification | compliance/evidence/tier4/candidates/ops-cli |  | — | — |
| par-jar-rar | par-jar-rar-client | hardening | RFC 9101, RFC 9126, RFC 9396, RFC 8707 | compliance/evidence/tier4/candidates/par-jar-rar |  | — | — |
| resource-server | resource-server | hardening | RFC 6750, RFC 7662, RFC 8693, RFC 8707, RFC 9068, RFC 9728, RFC 9700 | compliance/evidence/tier4/candidates/resource-server |  | — | — |
| rp-session-logout | rp-session-logout-rp | hardening | RFC 6265, OIDC Session Management, OIDC RP-Initiated Logout, OIDC Front-Channel Logout, OIDC Back-Channel Logout | compliance/evidence/tier4/candidates/rp-session-logout |  | — | — |
| runner-hypercorn | hypercorn-runner | production | ASGI 3 application package, Runner profile: Hypercorn | compliance/evidence/tier4/candidates/runner-hypercorn |  | — | — |
| runner-tigrcorn | tigrcorn-runner | production | ASGI 3 application package, Runner profile: Tigrcorn | compliance/evidence/tier4/candidates/runner-tigrcorn |  | — | — |
| runner-uvicorn | uvicorn-runner | production | ASGI 3 application package, Runner profile: Uvicorn | compliance/evidence/tier4/candidates/runner-uvicorn |  | — | — |
| spa | spa-rp | hardening | RFC 6749, RFC 7636, OIDC Core 1.0, OIDC Discovery 1.0 | compliance/evidence/tier4/candidates/spa |  | — | — |

Tier 4 claims are promoted only for targets backed by preserved external bundles with peer identity, version, container/runtime provenance, exact transcripts, complete scenario coverage, and reproduction material.
Repository-staged fixture bundles and self-attested bundle roots are preserved only for fail-closed validation exercises and never count toward strict independent claims.
