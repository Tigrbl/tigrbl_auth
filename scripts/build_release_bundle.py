from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tigrbl_auth.cli.artifacts import deployment_from_options
from tigrbl_auth.cli.reports import build_release_bundle


PROFILES = ("baseline", "production", "hardening", "peer-claim")


def main() -> int:
    bundles = []
    for profile in PROFILES:
        deployment = deployment_from_options(profile=profile)
        path = build_release_bundle(ROOT, deployment)
        bundles.append({"profile": profile, "bundle_dir": str(path.relative_to(ROOT))})
    print(json.dumps({"bundles": bundles}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
