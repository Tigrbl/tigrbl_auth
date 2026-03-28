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

# Boundary and Modularity Plan

## Certified core

The certified core is the release-eligible Tigrbl-native authn/z boundary. Only
modules in this boundary may back claimable RFC, OIDC, OpenAPI, or OpenRPC
surfaces.

It includes:
- OAuth 2.0 authorization-server endpoints
- OpenID Connect provider endpoints
- JOSE/JWT/JWK/JWKS
- discovery and `.well-known` metadata
- token lifecycle, sessions, cookies, logout, and client registration
- OpenAPI/OpenRPC contracts
- ADR, claims, evidence, and gate linkage when mapped to declared targets

## Governance plane

The governance plane holds CLI operators, verification scripts, claims/evidence
artifacts, and release-gate logic. It is not itself a certifiable protocol
surface, but it is required for certification evidence.

## Legacy transition

Legacy transition modules are explicitly non-certifiable. They exist only to
preserve continuity during the refactor. The release path may not claim RFC/OIDC
conformance on top of these modules.

## Extension quarantine

Extensions remain outside the certified core unless explicitly promoted with a
new ADR, target declaration, code/evidence mapping, and release-gate coverage.

## Alignment-only

Alignment-only items, such as OAuth 2.1 tracking, are never emitted as RFC
claims.

## Out of scope in baseline

The baseline boundary explicitly excludes:
- SAML IdP/SP
- LDAP/AD federation
- SCIM
- full authorization-policy platform
- Supabase-style data-plane authorization
- framework-local auth subsystem
- Keycloak-scale federation breadth

## Strict decisions

- only declared targets are certifiable
- runtime code is organized by domain/protocol planes instead of a flat RFC tree
- extensions remain outside the certified core unless promoted
- no direct FastAPI or Starlette imports or dependencies in supported paths
- only Tigrbl public APIs are allowed in release-path composition
- wrapper modules cannot back certified-core claims
- Tier 3 requires preserved evidence
- Tier 4 requires independent peer evidence

## Enforcement

The boundary is enforced by machine-checkable scans for:
- declared-target-only certification
- module boundary resolution
- imports that cross from certified core into legacy or extension boundaries
- FastAPI/Starlette and non-public Tigrbl leakage
- wrapper hygiene in certified-core paths
- contract drift across active and profile artifacts
- missing Tier 3 and Tier 4 evidence references

## Current posture

This checkpoint installs the boundary model and enforcement stack, and it also
records the remaining violations honestly. The package remains a governed
checkpoint until certified-core imports of legacy transition modules are
eliminated and the remaining production/hardening targets are implemented and
evidenced.
