<!-- NON_AUTHORITATIVE_HISTORICAL -->
> [!WARNING]
> Historical / non-authoritative checkpoint document.
> Do **not** use this file to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

> [!WARNING] Historical / non-authoritative document. This file is retained for provenance or implementation context only. Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports for current release truth.

> **Historical / non-authoritative** — This document is retained for planning or provenance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# TEST_COVERAGE_HEATMAP

Coverage counts are derived from `compliance/mappings/target-to-test.yaml` and the canonical `compliance/mappings/test_classification.yaml` manifest.

- target_count: `39`
- classified_test_count: `138`

| Target | Unit | Integration | Conformance | Interop | E2E | Security | Negative | Perf | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OIDC Back-Channel Logout | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 3 |
| OIDC Core 1.0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 4 |
| OIDC Discovery 1.0 | 0 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 7 |
| OIDC Front-Channel Logout | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 3 |
| OIDC RP-Initiated Logout | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 4 |
| OIDC Session Management | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 4 |
| OIDC UserInfo | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| OpenAPI 3.1 / 3.2 compatible public contract | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| OpenRPC 1.4.x admin/control-plane contract | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| RFC 6265 | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 4 |
| RFC 6749 | 0 | 3 | 2 | 3 | 0 | 0 | 0 | 0 | 8 |
| RFC 6750 | 0 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 5 |
| RFC 7009 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 5 |
| RFC 7515 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7516 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7517 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7518 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7519 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7521 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7523 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 7591 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 5 |
| RFC 7592 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 4 |
| RFC 7636 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 7662 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 5 |
| RFC 8252 | 1 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 5 |
| RFC 8414 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 8615 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| RFC 8628 | 1 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 8 |
| RFC 8693 | 1 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 8 |
| RFC 8705 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 8707 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| RFC 9068 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 9101 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 9126 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 9207 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| RFC 9396 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 9449 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 6 |
| RFC 9700 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| RFC 9728 | 1 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 6 |
