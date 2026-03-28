from __future__ import annotations

from pathlib import Path

from _surface_checks import verify_contract_sync, write_report

ROOT = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    payload = verify_contract_sync(ROOT)
    report = {
        "scope": "contract-sync",
        "strict": True,
        **payload,
    }
    write_report(ROOT / "docs" / "compliance", "contract_sync_report", report, "Contract Sync Report")
    raise SystemExit(1 if payload["failures"] else 0)
