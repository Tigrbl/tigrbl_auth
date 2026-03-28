from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tigrbl_auth.cli.reports import generate_state_reports, summarize_evidence_status


def main() -> int:
    payload = generate_state_reports(ROOT)
    summarize_evidence_status(ROOT)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_release_decision_record.py")], check=True)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
