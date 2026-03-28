from __future__ import annotations

from pathlib import Path

from _surface_checks import verify_test_classification_manifest, write_report

ROOT = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    payload = verify_test_classification_manifest(ROOT)
    report = {
        "scope": "test-classification",
        "strict": True,
        **payload,
    }
    write_report(ROOT / "docs" / "compliance", "test_classification_report", report, "Test Classification Report")
    raise SystemExit(1 if payload["failures"] else 0)
