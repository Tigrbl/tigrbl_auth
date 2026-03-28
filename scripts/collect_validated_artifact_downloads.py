from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _copy_tree(src: Path, dst: Path) -> list[str]:
    copied: list[str] = []
    if not src.exists():
        return copied
    for path in sorted(src.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(str(rel))
    return copied


def collect_validated_artifact_downloads(
    repo_root: Path,
    *,
    download_root: Path,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    download_root = download_root.resolve()

    if not download_root.exists():
        return {
            "passed": False,
            "download_root_present": False,
            "download_root": str(download_root),
            "artifact_count": 0,
            "validated_manifest_count": 0,
            "runtime_smoke_file_count": 0,
            "install_substrate_file_count": 0,
            "runtime_profile_file_count": 0,
            "test_report_file_count": 0,
            "migration_file_count": 0,
            "compliance_report_file_count": 0,
            "artifacts": [],
        }

    validated_root = repo_root / "dist" / "validated-runs"
    runtime_smoke_root = repo_root / "dist" / "runtime-smoke" / "collected"
    install_root = repo_root / "dist" / "install-substrate" / "collected"
    runtime_profile_root = repo_root / "dist" / "runtime-profiles" / "collected"
    test_report_root = repo_root / "dist" / "test-reports" / "collected"
    migration_root = repo_root / "dist" / "migration-portability" / "collected"
    compliance_root = repo_root / "docs" / "compliance" / "collected"
    validated_root.mkdir(parents=True, exist_ok=True)
    runtime_smoke_root.mkdir(parents=True, exist_ok=True)
    install_root.mkdir(parents=True, exist_ok=True)
    runtime_profile_root.mkdir(parents=True, exist_ok=True)
    test_report_root.mkdir(parents=True, exist_ok=True)
    migration_root.mkdir(parents=True, exist_ok=True)
    compliance_root.mkdir(parents=True, exist_ok=True)

    artifact_summaries: list[dict[str, Any]] = []
    validated_manifest_count = 0
    runtime_smoke_file_count = 0
    install_substrate_file_count = 0
    runtime_profile_file_count = 0
    test_report_file_count = 0
    migration_file_count = 0
    compliance_report_file_count = 0
    empty_artifacts: list[str] = []

    for artifact_dir in sorted(path for path in download_root.iterdir() if path.is_dir()):
        label = artifact_dir.name
        summary: dict[str, Any] = {
            "artifact": label,
            "source": _relative(artifact_dir, repo_root),
            "validated_manifests": [],
            "runtime_smoke_files": [],
            "install_substrate_files": [],
            "runtime_profile_files": [],
            "test_report_files": [],
            "migration_files": [],
            "compliance_report_files": [],
        }

        manifest_dir = artifact_dir / "dist" / "validated-runs"
        for manifest in sorted(manifest_dir.glob("*.json")):
            target = validated_root / manifest.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(manifest, target)
            summary["validated_manifests"].append(str(manifest.name))
            validated_manifest_count += 1

        smoke_files = _copy_tree(artifact_dir / "dist" / "runtime-smoke", runtime_smoke_root / label)
        runtime_smoke_file_count += len(smoke_files)
        summary["runtime_smoke_files"].extend(smoke_files)

        install_files = _copy_tree(artifact_dir / "dist" / "install-substrate", install_root / label)
        install_substrate_file_count += len(install_files)
        summary["install_substrate_files"].extend(install_files)

        runtime_profile_files = _copy_tree(artifact_dir / "dist" / "runtime-profiles", runtime_profile_root / label)
        runtime_profile_file_count += len(runtime_profile_files)
        summary["runtime_profile_files"].extend(runtime_profile_files)

        test_report_files = _copy_tree(artifact_dir / "dist" / "test-reports", test_report_root / label)
        test_report_file_count += len(test_report_files)
        summary["test_report_files"].extend(test_report_files)

        migration_files = _copy_tree(artifact_dir / "dist" / "migration-portability", migration_root / label)
        migration_file_count += len(migration_files)
        summary["migration_files"].extend(migration_files)

        compliance_files = _copy_tree(artifact_dir / "docs" / "compliance", compliance_root / label)
        compliance_report_file_count += len(compliance_files)
        summary["compliance_report_files"].extend(compliance_files)

        if not any(
            summary[key]
            for key in (
                "validated_manifests",
                "runtime_smoke_files",
                "install_substrate_files",
                "runtime_profile_files",
                "test_report_files",
                "migration_files",
                "compliance_report_files",
            )
        ):
            empty_artifacts.append(label)

        artifact_summaries.append(summary)

    payload = {
        "passed": bool(artifact_summaries) and not empty_artifacts,
        "download_root_present": True,
        "download_root": _relative(download_root, repo_root),
        "artifact_count": len(artifact_summaries),
        "validated_manifest_count": validated_manifest_count,
        "runtime_smoke_file_count": runtime_smoke_file_count,
        "install_substrate_file_count": install_substrate_file_count,
        "runtime_profile_file_count": runtime_profile_file_count,
        "test_report_file_count": test_report_file_count,
        "migration_file_count": migration_file_count,
        "compliance_report_file_count": compliance_report_file_count,
        "empty_artifact_count": len(empty_artifacts),
        "empty_artifacts": empty_artifacts,
        "artifacts": artifact_summaries,
    }
    report_path = validated_root / "collected-artifact-downloads.json"
    report_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    payload["report_path"] = _relative(report_path, repo_root)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize downloaded GitHub Actions validated-artifact trees into repository dist/ paths.")
    parser.add_argument("--repo-root", default=str(ROOT), help="Repository root receiving the normalized artifacts.")
    parser.add_argument(
        "--download-root",
        default=str(ROOT / ".artifacts" / "validated-downloads"),
        help="Root directory produced by actions/download-artifact when validated artifacts are downloaded without merge-multiple.",
    )
    parser.add_argument(
        "--if-present",
        action="store_true",
        help="Return success with a skipped payload when the download root does not exist.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    download_root = Path(args.download_root).resolve()
    if args.if_present and not download_root.exists():
        payload = {
            "passed": True,
            "skipped": True,
            "message": "Download root is not present; nothing to collect.",
            "download_root": str(download_root),
        }
        print(json.dumps(payload, indent=2))
        return 0

    payload = collect_validated_artifact_downloads(repo_root, download_root=download_root)
    print(json.dumps(payload, indent=2))
    return 0 if payload.get("passed", False) else 1


if __name__ == "__main__":
    raise SystemExit(main())
