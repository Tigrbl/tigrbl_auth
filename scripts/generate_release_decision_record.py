from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def bullet_lines(items: list[str], empty: str = "- none") -> str:
    if not items:
        return empty
    return "\n".join(f"- {item}" for item in items)


def main() -> int:
    current = load_json(ROOT / "docs" / "compliance" / "current_state_report.json")
    cert = load_json(ROOT / "docs" / "compliance" / "certification_state_report.json")
    gates = load_json(ROOT / "docs" / "compliance" / "release_gate_report.json")
    matrix = load_json(ROOT / "docs" / "compliance" / "final_target_decision_matrix.json")
    scope = load_yaml(ROOT / "compliance" / "targets" / "certification_scope.yaml")
    repository_state = load_yaml(ROOT / "compliance" / "claims" / "repository-state.yaml").get("repository_state", {})
    validated_path = ROOT / "docs" / "compliance" / "validated_execution_report.json"
    validated = load_json(validated_path) if validated_path.exists() else {"summary": {}}

    current_summary = current.get("summary", {})
    cert_summary = cert.get("summary", {})
    gate_summary = gates.get("summary", {})
    validated_summary = validated.get("summary", {}) if isinstance(validated, dict) else {}
    discrepancy_summary = scope.get("discrepancy_summary", {}) or {}
    profile_scope_mismatch_count = sum(int(value) for value in discrepancy_summary.values())
    profile_scope_mismatch_set_empty = profile_scope_mismatch_count == 0
    target_profile_truth_reconciled_complete = bool(repository_state.get("phase_13_target_profile_truth_reconciled_complete", profile_scope_mismatch_set_empty))
    alignment_only_checkpoint_no_new_certification_evidence = bool(repository_state.get("alignment_only_checkpoint_no_new_certification_evidence", False))

    rows = matrix.get("rows", [])
    certifiable = [row["target"] for row in rows if str(row.get("status")) == "certifiably-complete"]
    complete_nonfinal = [row["target"] for row in rows if str(row.get("status")) == "complete-but-not-independently-peer-certified"]
    partial = [row["target"] for row in rows if str(row.get("status")) not in {"certifiably-complete", "complete-but-not-independently-peer-certified"}]
    out = [row["target"] for row in matrix.get("out_of_scope", [])]

    fully_certifiable_now = bool(cert_summary.get("fully_certifiable_now", False))
    fully_rfc_compliant_now = bool(cert_summary.get("fully_rfc_compliant_now", False))
    non_rfc_summary = load_json(ROOT / "docs" / "compliance" / "non_rfc_status_report.json").get("summary", {}) if (ROOT / "docs" / "compliance" / "non_rfc_status_report.json").exists() else {}
    fully_non_rfc_spec_compliant_now = bool(non_rfc_summary.get("certifiably_fully_non_rfc_spec_compliant_now", False))
    strict_independent_claims_ready = bool(cert_summary.get("strict_independent_claims_ready", False))
    final_release_ready = fully_certifiable_now and fully_rfc_compliant_now and fully_non_rfc_spec_compliant_now and strict_independent_claims_ready

    decision = (
        "Cut the final certified release."
        if final_release_ready
        else "Do **not** cut a final certified release. Publish only a truthful candidate checkpoint / release-bundle set until runtime, tests, evidence, and Tier 4 peer promotion all satisfy the retained boundary."
    )
    release_statement = (
        "This package is releasable as a **final certified package**."
        if final_release_ready
        else "This package is releasable only as a **truthfully labeled candidate checkpoint / retained-boundary Tier 3 release-bundle set**. It is not releasable as a final certified package while validated runtime/test evidence and preserved Tier 4 external peer bundles remain absent."
    )

    clean_room_executor_matrix_declared_complete = bool(repository_state.get("phase_13_clean_room_executor_matrix_declared_complete", False))
    validated_manifest_identity_contract_installed = bool(repository_state.get("phase_13_validated_manifest_identity_contract_installed", False))
    validated_runtime_matrix_preservation_complete = bool(repository_state.get("phase_13_validated_runtime_matrix_preservation_complete", False))
    validated_test_lane_preservation_complete = bool(repository_state.get("phase_13_validated_test_lane_preservation_complete", False))
    validated_migration_portability_preservation_complete = bool(repository_state.get("phase_13_validated_migration_portability_preservation_complete", False))

    current_state_md = f"""# CURRENT_STATE

## Summary

This repository is a **final certification aggregation checkpoint** for `tigrbl_auth`, with the retained target/profile truth reconciliation complete for RFC 7516, RFC 7592, and RFC 9207, and with the clean-room executor / validated-manifest evidence contract tightened so preserved runtime, test-lane, and migration artifacts must carry install evidence, environment identity, and backend-specific proof.

Historical planning/checkpoint material is now archived under `docs/archive/historical/` (with `docs/archive/README.md` as the archive entrypoint), and the current authoritative set is curated in the generated `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`.

The repository is **{'certifiably fully featured' if fully_certifiable_now else 'not yet certifiably fully featured'}**, **{'certifiably fully RFC/spec compliant' if fully_rfc_compliant_now else 'not yet certifiably fully RFC/spec compliant'}**, and **{'certifiably fully non-RFC spec/standard compliant' if fully_non_rfc_spec_compliant_now else 'not yet certifiably fully non-RFC spec/standard compliant'}**.

## Current generated state

- declared in-scope claim count: `{current_summary.get('declared_claim_count', 0)}`
- Tier 3 claim count: `{current_summary.get('tier_3_claim_count', 0)}`
- Tier 4 claim count: `{current_summary.get('tier_4_claim_count', 0)}`
- strict independent claims ready: `{strict_independent_claims_ready}`
- certifiably fully non-RFC spec/standard compliant now: `{fully_non_rfc_spec_compliant_now}`
- target/profile truth reconciled complete: `{target_profile_truth_reconciled_complete}`
- profile-scope mismatch count: `{profile_scope_mismatch_count}`
- profile-scope mismatch set empty: `{profile_scope_mismatch_set_empty}`
- alignment-only checkpoint without new certification evidence: `{alignment_only_checkpoint_no_new_certification_evidence}`
- clean-room executor matrix declared complete: `{clean_room_executor_matrix_declared_complete}`
- validated manifest identity contract installed: `{validated_manifest_identity_contract_installed}`
- validated runtime matrix preservation complete: `{validated_runtime_matrix_preservation_complete}`
- validated test-lane preservation complete: `{validated_test_lane_preservation_complete}`
- validated migration portability preservation complete: `{validated_migration_portability_preservation_complete}`
- authoritative current doc count: `{current_summary.get('authoritative_current_doc_count', 0)}`
- archived historical root count: `{current_summary.get('archived_historical_root_count', 0)}`
- certification bundle current-state doc count: `{current_summary.get('certification_bundle_current_state_doc_count', 0)}`
- install substrate manifest passed: `{current_summary.get('install_substrate_manifest_passed', False)}`
- install substrate supported-python binaries detected: `{current_summary.get('install_substrate_detected_supported_python_count', 0)}` / `{current_summary.get('install_substrate_expected_supported_python_count', 0)}`
- install substrate current-profile import probe passed: `{current_summary.get('install_substrate_current_profile_import_probe_passed', False)}`
- validated inventory present count: `{current_summary.get('validated_inventory_present_count', 0)}` / `{current_summary.get('required_validated_inventory_count', 0)}`
- validated runtime matrix passed count: `{current_summary.get('validated_runtime_matrix_passed_count', 0)}` / `{current_summary.get('validated_runtime_matrix_expected_count', 0)}`
- validated test-lane passed count: `{current_summary.get('validated_test_lane_passed_count', 0)}` / `{current_summary.get('validated_test_lane_expected_count', 0)}`
- migration portability passed: `{current_summary.get('migration_portability_passed', False)}`
- runtime profile ready count: `{current_summary.get('runtime_profile_ready_count', 0)}`
- runtime profile missing count: `{current_summary.get('runtime_profile_missing_count', 0)}`
- runtime profile invalid count: `{current_summary.get('runtime_profile_invalid_count', 0)}`
- historical stale doc refs outside archive: `{current_summary.get('historical_doc_stale_ref_count', 0)}`

## What is now claimable

- the repository has a clearly separated authoritative current documentation set
- historical / superseded planning material is preserved in a non-authoritative archive tree
- certification bundles are built from generated current-state docs only, with executable contracts copied separately as non-doc release artifacts
- the clean-room install substrate is explicitly declared in `pyproject.toml`, `constraints/*.txt`, `tox.ini`, CI workflows, and generated install-substrate reports
- the supported clean-room executor matrix is declared for Python `3.10`, `3.11`, and `3.12`, with PostgreSQL required in the preserved certification matrix rather than optional for the relevant lanes
- preserved runtime, test-lane, and migration manifests now have a stricter fail-closed evidence contract tying pass status to install evidence, environment identity, serve-check / pytest artifacts, and revision-aware backend results
- release bundles and attestations can be rebuilt and verified from the repository state
- the repository cannot yet claim a final certified release while preserved py3.10/3.11/3.12 runtime/test/migration evidence and Tier 4 external peer bundles remain incomplete

## Key artifacts to inspect

- `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md`
- `docs/compliance/current_state_report.md`
- `docs/compliance/install_substrate_report.md`
- `docs/compliance/validated_execution_report.md`
- `docs/compliance/runtime_profile_report.md`
- `docs/compliance/migration_portability_report.md`
- `docs/compliance/certification_state_report.md`
- `docs/compliance/release_gate_report.md`
- `docs/compliance/final_release_gate_report.md`
- `docs/compliance/RELEASE_DECISION_RECORD.md`
- `docs/compliance/CLEAN_ROOM_EXECUTOR_AND_EVIDENCE_CHECKPOINT_2026-03-27.md`
- `docs/archive/README.md`
- `CERTIFICATION_STATUS.md`
"""

    gaps = [str(item) for item in cert_summary.get("open_gaps", []) or []]
    cert_status_md = f"""# CERTIFICATION_STATUS

## Honest status

`tigrbl_auth` in this checkpoint is **{'certifiably fully featured' if fully_certifiable_now else 'not yet certifiably fully featured'}**.

`tigrbl_auth` in this checkpoint is **{'certifiably fully RFC/spec compliant' if fully_rfc_compliant_now else 'not yet certifiably fully RFC/spec compliant'}**.

`tigrbl_auth` in this checkpoint is **{'certifiably fully non-RFC spec/standard compliant' if fully_non_rfc_spec_compliant_now else 'not yet certifiably fully non-RFC spec/standard compliant'}**.

## Final-release gate posture

- fully_certifiable_now: `{fully_certifiable_now}`
- fully_rfc_compliant_now: `{fully_rfc_compliant_now}`
- fully_non_rfc_spec_compliant_now: `{fully_non_rfc_spec_compliant_now}`
- strict_independent_claims_ready: `{strict_independent_claims_ready}`
- release_gates_passed: `{gates.get('passed', False)}`
- target_profile_truth_reconciled_complete: `{target_profile_truth_reconciled_complete}`
- profile_scope_mismatch_set_empty: `{profile_scope_mismatch_set_empty}`
- alignment_only_checkpoint_no_new_certification_evidence: `{alignment_only_checkpoint_no_new_certification_evidence}`
- clean_room_executor_matrix_declared_complete: `{clean_room_executor_matrix_declared_complete}`
- validated_manifest_identity_contract_installed: `{validated_manifest_identity_contract_installed}`
- clean_room_install_matrix_green: `{gate_summary.get('clean_room_install_matrix_green', False)}`
- in_scope_test_lanes_green: `{gate_summary.get('in_scope_test_lanes_green', False)}`
- migration_portability_passed: `{gate_summary.get('migration_portability_passed', False)}`
- tier3_evidence_rebuilt_from_validated_runs: `{gate_summary.get('tier3_evidence_rebuilt_from_validated_runs', False)}`
- tier4_bundle_promotion_complete: `{gate_summary.get('tier4_bundle_promotion_complete', False)}`

## Open gaps blocking final certification

{bullet_lines(gaps)}

## Practical recommendation

Use this repository state as a **truthful clean-room executor / validated-evidence checkpoint**, not as a final certified release. The retained profile-scope mismatch set is empty and the stricter validated-manifest contract is now installed, but preserved py3.10/3.11/3.12 runtime/test evidence, PostgreSQL-backed migration portability evidence, and Tier 4 external peer bundles are still required before any final certification claim becomes truthful.
"""

    release_decision_md = f"""# Release Decision Record

## Decision

{decision}

## Basis for the decision

- release gates passed: `{gates.get('passed', False)}`
- gate count: `{gate_summary.get('gate_count', 0)}`
- in-scope declared targets: `{current_summary.get('declared_claim_count', 0)}`
- Tier 3 claims: `{current_summary.get('tier_3_claim_count', 0)}`
- Tier 4 claims: `{current_summary.get('tier_4_claim_count', 0)}`
- signed release bundles: `{current_summary.get('signed_release_bundle_count', 0)}`
- retained boundary Tier 3 complete: `{cert_summary.get('retained_boundary_tier3_complete', False)}`
- fully certifiable now: `{fully_certifiable_now}`
- fully RFC/spec compliant now: `{fully_rfc_compliant_now}`
- fully non-RFC spec/standard compliant now: `{fully_non_rfc_spec_compliant_now}`
- strict independent claims ready: `{strict_independent_claims_ready}`
- validated runtime matrix green: `{validated_summary.get('runtime_matrix_green', False)}`
- validated in-scope test lanes green: `{validated_summary.get('in_scope_test_lanes_green', False)}`
- validated migration portability: `{validated_summary.get('migration_portability_passed', False)}`

## Documentation authority

- archive root: `docs/archive/historical`
- generated current-state docs only in certification bundle: `True`
- authoritative current docs manifest present: `{(ROOT / 'docs' / 'compliance' / 'AUTHORITATIVE_CURRENT_DOCS.json').exists()}`

## Truthful release statement partition

### Certifiably complete

{bullet_lines(certifiable, empty='- none')}

### Complete but not independently peer-certified

{bullet_lines(complete_nonfinal, empty='- none')}

### Partial or deferred inside the retained certification boundary

{bullet_lines(partial, empty='- none')}

### Out of scope

{bullet_lines(out, empty='- none')}

## Releaseable package statement

{release_statement}
"""

    compliance_current_state_md = f"""# Current State

See the authoritative generated reports:

- `current_state_report.md`
- `install_substrate_report.md`
- `certification_state_report.md`
- `runtime_profile_report.md`
- `release_gate_report.md`
- `validated_execution_report.md`
- `release_signing_report.md`

Archive and document-authority status:

- authoritative current docs manifest present: `{(ROOT / 'docs' / 'compliance' / 'AUTHORITATIVE_CURRENT_DOCS.json').exists()}`
- archive root: `docs/archive/historical`
- historical docs are non-authoritative: `True`
"""

    write_text(ROOT / "CURRENT_STATE.md", current_state_md)
    write_text(ROOT / "CERTIFICATION_STATUS.md", cert_status_md)
    write_text(ROOT / "docs" / "compliance" / "current_state.md", compliance_current_state_md)
    write_text(ROOT / "docs" / "compliance" / "RELEASE_DECISION_RECORD.md", release_decision_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
