from __future__ import annotations

from pathlib import Path

from _surface_checks import verify_target_route_mapping, write_report

ROOT = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    payload = verify_target_route_mapping(ROOT)
    write_report(ROOT / "docs" / "compliance", "target_route_mapping_report", payload, "Target to Route Mapping Report")
    raise SystemExit(1 if payload["failures"] else 0)
