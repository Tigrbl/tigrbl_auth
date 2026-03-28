from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RUNTIME_IMPORTS = [
    "tigrbl",
    "sqlalchemy",
    "uvicorn",
    "hypercorn",
    "tigrcorn",
]


@dataclass(frozen=True)
class BundleSpec:
    target: str
    bundle_dir: str
    profile: str
    contracts: list[str]
    reports: list[str]
    tests: list[str]


BUNDLE_SPECS = [
    BundleSpec(
        target="ASGI 3 application package",
        bundle_dir="compliance/evidence/tier3/asgi-application",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
            "docs/compliance/runtime_profile_report.json",
            "specs/openapi/profiles/baseline/tigrbl_auth.public.openapi.json",
            "specs/openrpc/profiles/baseline/tigrbl_auth.admin.openrpc.json",
            "specs/discovery/profiles/baseline/openid-configuration.json",
            "specs/discovery/profiles/baseline/oauth-authorization-server.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/runtime_profile_report.json",
            "docs/compliance/runtime_profile_report.md",
            "docs/compliance/evidence_status_report.json",
            "docs/compliance/evidence_status_report.md",
            "docs/compliance/target_module_mapping_report.json",
            "docs/compliance/target_module_mapping_report.md",
            "docs/compliance/target_test_mapping_report.json",
            "docs/compliance/target_test_mapping_report.md",
            "docs/compliance/target_evidence_mapping_report.json",
            "docs/compliance/target_evidence_mapping_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/runtime/test_runner_invariance.py",
            "tests/conformance/operator/test_cli_serve_runtime.py",
        ],
    ),
    BundleSpec(
        target="Runner profile: Uvicorn",
        bundle_dir="compliance/evidence/tier3/runner-uvicorn",
        profile="baseline",
        contracts=[
            "docs/compliance/runtime_profile_report.json",
            "specs/cli/cli_contract.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/runtime_profile_report.json",
            "docs/compliance/runtime_profile_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/runtime/test_runner_uvicorn.py",
            "tests/conformance/operator/test_cli_serve_runtime.py",
            "tests/interop/test_runner_profile_catalog_completeness.py",
        ],
    ),
    BundleSpec(
        target="Runner profile: Hypercorn",
        bundle_dir="compliance/evidence/tier3/runner-hypercorn",
        profile="baseline",
        contracts=[
            "docs/compliance/runtime_profile_report.json",
            "specs/cli/cli_contract.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/runtime_profile_report.json",
            "docs/compliance/runtime_profile_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/runtime/test_runner_hypercorn.py",
            "tests/conformance/operator/test_cli_serve_runtime.py",
            "tests/interop/test_runner_profile_catalog_completeness.py",
        ],
    ),
    BundleSpec(
        target="Runner profile: Tigrcorn",
        bundle_dir="compliance/evidence/tier3/runner-tigrcorn",
        profile="baseline",
        contracts=[
            "docs/compliance/runtime_profile_report.json",
            "specs/cli/cli_contract.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/runtime_profile_report.json",
            "docs/compliance/runtime_profile_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/runtime/test_runner_tigrcorn.py",
            "tests/conformance/operator/test_cli_serve_runtime.py",
            "tests/interop/test_runner_profile_catalog_completeness.py",
        ],
    ),
    BundleSpec(
        target="CLI operator surface",
        bundle_dir="compliance/evidence/tier3/cli-operator-surface",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
            "docs/reference/CLI_SURFACE.md",
            "specs/openrpc/profiles/baseline/tigrbl_auth.admin.openrpc.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/cli_conformance_snapshot.json",
            "docs/compliance/cli_conformance_snapshot.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/conformance/operator/test_cli_resource_lifecycle.py",
            "tests/conformance/operator/test_cli_serve_runtime.py",
            "tests/interop/test_operator_profile_catalog_completeness.py",
        ],
    ),
    BundleSpec(
        target="Bootstrap and migration lifecycle",
        bundle_dir="compliance/evidence/tier3/bootstrap-migration",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
            "docs/reference/CLI_SURFACE.md",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/cli_conformance_snapshot.json",
            "docs/compliance/cli_conformance_snapshot.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=["tests/conformance/operator/test_cli_bootstrap_migrate.py"],
    ),
    BundleSpec(
        target="Key lifecycle and JWKS publication",
        bundle_dir="compliance/evidence/tier3/key-lifecycle-jwks",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
            "specs/discovery/profiles/baseline/jwks.json",
            "specs/discovery/profiles/baseline/oauth-authorization-server.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/conformance/operator/test_cli_keys_lifecycle.py",
            "tests/security/test_phase12_sender_constraint_replay.py",
        ],
    ),
    BundleSpec(
        target="Import/export portability",
        bundle_dir="compliance/evidence/tier3/import-export-portability",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=["tests/conformance/operator/test_cli_import_export.py"],
    ),
    BundleSpec(
        target="Release bundle and signature verification",
        bundle_dir="compliance/evidence/tier3/release-bundle-signing",
        profile="baseline",
        contracts=[
            "specs/cli/cli_contract.json",
            "dist/release-bundles/0.3.2.dev14/baseline/release-bundle.json",
            "dist/release-bundles/0.3.2.dev14/baseline/signature.json",
            "dist/release-bundles/0.3.2.dev14/baseline/verification.json",
        ],
        reports=[
            "docs/compliance/current_state_report.json",
            "docs/compliance/current_state_report.md",
            "docs/compliance/certification_state_report.json",
            "docs/compliance/certification_state_report.md",
            "docs/compliance/release_gate_report.json",
            "docs/compliance/release_gate_report.md",
            "docs/compliance/phase12_targeted_test_output.txt",
        ],
        tests=[
            "tests/security/test_release_bundle_signing.py",
            "tests/conformance/operator/test_cli_bootstrap_migrate.py",
        ],
    ),
]


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _write_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _copy(rel_path: str, bundle_root: Path, subdir: str) -> str:
    src = ROOT / rel_path
    if not src.exists():
        raise FileNotFoundError(f"Missing required artifact for bundle generation: {rel_path}")
    dst = bundle_root / subdir / Path(rel_path).name
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())
    return str(dst.relative_to(bundle_root))


def _bundle_modules(target: str) -> list[str]:
    mapping = yaml.safe_load((ROOT / "compliance" / "mappings" / "target-to-module.yaml").read_text(encoding="utf-8"))
    value = mapping.get(target, [])
    if isinstance(value, dict):
        value = value.get("modules", [])
    return [str(item) for item in value]


def _package_version() -> str:
    pyproject = ROOT / "pyproject.toml"
    text = pyproject.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.strip().startswith("version = "):
            return line.split("=", 1)[1].strip().strip('"')
    return "unknown"


def _missing_runtime_imports() -> list[str]:
    missing: list[str] = []
    for name in RUNTIME_IMPORTS:
        if importlib.util.find_spec(name) is None:
            missing.append(name)
    return missing


def _source_zip() -> str | None:
    candidates = [
        Path("/mnt/data/tigrbl_auth_phase13_phase11_truthfulness_checkpoint.zip"),
        Path("/mnt/data/tigrbl_auth_phase13_phase10_hardening_cluster_c_checkpoint.zip"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def materialize_bundle(spec: BundleSpec) -> None:
    bundle_root = ROOT / spec.bundle_dir
    if bundle_root.exists():
        for child in sorted(bundle_root.rglob("*"), reverse=True):
            if child.is_file() or child.is_symlink():
                child.unlink()
            elif child.is_dir():
                try:
                    child.rmdir()
                except OSError:
                    pass
    bundle_root.mkdir(parents=True, exist_ok=True)

    copied_contracts = [_copy(path, bundle_root, "contracts") for path in spec.contracts]
    copied_reports = [_copy(path, bundle_root, "reports") for path in spec.reports]

    readme = f"""# Tier 3 evidence bundle — {spec.target}

This preserved bundle was materialized during the Phase 12 retained-boundary Tier 3 closeout.

- target: `{spec.target}`
- profile: `{spec.profile}`
- bundle dir: `{spec.bundle_dir}`
- capture mode: `dependency-light runtime/operator preserved evidence`

The bundle preserves contract artifacts, generated reports, and targeted runtime/operator/security/interop test evidence sufficient for repository-attested Tier 3 promotion.
"""
    (bundle_root / "README.md").write_text(readme, encoding="utf-8")

    test_log = (ROOT / "docs" / "compliance" / "phase12_targeted_test_output.txt").read_text(encoding="utf-8")
    execution_log = f"""Phase 12 retained-boundary Tier 3 closeout execution log
Generated at: {now()}
Target: {spec.target}
Profile: {spec.profile}
Source checkpoint: {_source_zip() or 'unknown'}

Primary verification commands:
- python scripts/generate_effective_release_manifests.py
- python scripts/generate_state_reports.py
- pytest -q tests/runtime/test_runner_uvicorn.py tests/runtime/test_runner_hypercorn.py tests/runtime/test_runner_tigrcorn.py tests/runtime/test_runner_invariance.py tests/conformance/operator/test_cli_serve_runtime.py tests/conformance/operator/test_cli_resource_lifecycle.py tests/conformance/operator/test_cli_keys_lifecycle.py tests/conformance/operator/test_cli_import_export.py tests/conformance/operator/test_cli_bootstrap_migrate.py tests/negative/test_phase12_invalid_artifact_inputs.py tests/negative/test_phase12_resource_exchange_abuse.py tests/security/test_phase12_sender_constraint_replay.py tests/interop/test_peer_profile_catalog.py tests/interop/test_runner_profile_catalog_completeness.py tests/interop/test_operator_profile_catalog_completeness.py
- python scripts/run_release_gates.py

Target-associated tests:
""" + "\n".join(f"- {path}" for path in spec.tests) + "\n\nTargeted Phase 12 transcript:\n\n" + test_log
    (bundle_root / "execution.log").write_text(execution_log, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "generated_at": now(),
        "phase": "P13-phase12-checkpoint",
        "targets": [spec.target],
        "profile": spec.profile,
        "status": "evidenced-release-gated",
        "capture_mode": "dependency-light runtime/operator preserved evidence",
        "source_checkpoint_zip": _source_zip(),
        "evidence_dir": spec.bundle_dir,
    }
    mapping = {
        "targets": [spec.target],
        "modules": _bundle_modules(spec.target),
        "tests": spec.tests,
        "contracts": copied_contracts,
        "reports": copied_reports,
    }
    environment = {
        "generated_at": now(),
        "generator": "phase12-runtime-operator-bundle-writer",
        "python": sys.version,
        "platform": platform.platform(),
        "package_version": _package_version(),
        "source_checkpoint_zip": _source_zip(),
        "profile": spec.profile,
        "missing_runtime_modules": _missing_runtime_imports(),
        "evidence_dir": spec.bundle_dir,
    }
    _write_yaml(bundle_root / "manifest.yaml", manifest)
    _write_yaml(bundle_root / "mapping.yaml", mapping)
    _write_yaml(bundle_root / "environment.yaml", environment)

    hashes: dict[str, str] = {}
    for path in sorted(bundle_root.rglob("*")):
        if path.is_file() and path.name not in {"hashes.yaml", "signatures.yaml"}:
            hashes[str(path.relative_to(bundle_root))] = _sha256_file(path)
    _write_yaml(bundle_root / "hashes.yaml", {"sha256": hashes})
    _write_yaml(
        bundle_root / "signatures.yaml",
        {
            "mode": "internal-sha256-digest-only",
            "externally_attested": False,
            "note": "Certification-grade external peer signing remains outstanding; this checkpoint stores internal digests only.",
            "manifest_sha256": _sha256_file(bundle_root / "manifest.yaml"),
        },
    )


def main() -> int:
    for spec in BUNDLE_SPECS:
        materialize_bundle(spec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
