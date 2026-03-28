> [!WARNING] Non-authoritative active document. For current release and certification truth, use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` and the generated current-state reports.

> **Historical / non-authoritative** — This document is retained for planning, provenance, or operator guidance only.
> Do **not** use it to determine the current certification state, executable surface, or release readiness.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`, `CURRENT_STATE.md`, and `CERTIFICATION_STATUS.md` instead.

# CLI and Release Automation Runbook

1. `python scripts/generate_cli_docs.py`
2. `python scripts/generate_openapi_contract.py`
3. `python scripts/generate_openrpc_contract.py`
4. `python scripts/validate_openapi_contract.py`
5. `python scripts/validate_openrpc_contract.py`
6. `python scripts/build_evidence_bundle.py`
7. `python scripts/execute_peer_profiles.py`
8. `python scripts/build_release_bundle.py`
9. `python scripts/sign_release_bundle.py`
10. `python scripts/verify_release_signing.py`
11. `python scripts/run_release_gates.py`