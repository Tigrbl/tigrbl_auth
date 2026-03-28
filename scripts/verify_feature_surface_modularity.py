from __future__ import annotations

from pathlib import Path

from _surface_checks import verify_feature_surface_modularity, write_report

ROOT = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    payload = verify_feature_surface_modularity(ROOT)
    report = {
        "scope": "feature-flags-targets-public-surface-modularity",
        "strict": True,
        **payload,
    }
    write_report(
        ROOT / "docs" / "compliance",
        "feature_flags_surface_modularity_report",
        report,
        "Feature Flags, Targets, Surface, and Modularity Report",
    )
    raise SystemExit(1 if payload["failures"] else 0)
