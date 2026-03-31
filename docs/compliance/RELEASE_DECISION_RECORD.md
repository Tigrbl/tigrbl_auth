# Release Decision Record

## Decision

Do **not** cut a final certified release. Publish only a truthful candidate checkpoint / release-bundle set until runtime, tests, evidence, and Tier 4 peer promotion all satisfy the retained boundary.

## Basis for the decision

- release gates passed: `False`
- gate count: `20`
- in-scope declared targets: `48`
- Tier 3 claims: `48`
- Tier 4 claims: `0`
- signed release bundles: `4`
- retained boundary Tier 3 complete: `True`
- fully certifiable now: `False`
- fully RFC/spec compliant now: `False`
- fully non-RFC spec/standard compliant now: `False`
- strict independent claims ready: `False`
- validated runtime matrix green: `True`
- validated in-scope test lanes green: `True`
- validated migration portability: `True`

## Documentation authority

- archive root: `docs/archive/historical`
- generated current-state docs only in certification bundle: `True`
- authoritative current docs manifest present: `True`

## Truthful release statement partition

### Certifiably complete

- none

### Complete but not independently peer-certified

- RFC 6749
- RFC 6750
- RFC 7636
- RFC 8414
- RFC 8615
- RFC 7515
- RFC 7516
- RFC 7517
- RFC 7518
- RFC 7519
- RFC 7009
- RFC 7591
- RFC 7592
- RFC 7662
- RFC 8252
- RFC 8628
- RFC 8693
- RFC 8705
- RFC 8707
- RFC 9068
- RFC 9101
- RFC 9126
- RFC 9207
- RFC 9396
- RFC 9449
- RFC 6265
- RFC 7521
- RFC 7523
- RFC 9728
- RFC 9700
- OIDC Core 1.0
- OIDC Discovery 1.0
- OIDC UserInfo
- OIDC Session Management
- OIDC RP-Initiated Logout
- OIDC Front-Channel Logout
- OIDC Back-Channel Logout
- OpenAPI 3.1 / 3.2 compatible public contract
- OpenRPC 1.4.x admin/control-plane contract
- ASGI 3 application package
- Runner profile: Uvicorn
- Runner profile: Hypercorn
- Runner profile: Tigrcorn
- CLI operator surface
- Bootstrap and migration lifecycle
- Key lifecycle and JWKS publication
- Import/export portability
- Release bundle and signature verification

### Partial or deferred inside the retained certification boundary

- none

### Out of scope

- RFC 7800
- RFC 7952
- RFC 8291
- RFC 8812
- RFC 8932
- OAuth 2.1 alignment profile
- SAML IdP/SP
- LDAP/AD federation
- SCIM
- full authorization-policy platform
- Supabase-style data-plane authorization
- framework-local auth subsystem
- Keycloak-scale federation breadth

## Releaseable package statement

This package is releasable only as a **truthfully labeled candidate checkpoint / retained-boundary Tier 3 release-bundle set**. It is not releasable as a final certified package while validated runtime/test evidence and preserved Tier 4 external peer bundles remain absent.
