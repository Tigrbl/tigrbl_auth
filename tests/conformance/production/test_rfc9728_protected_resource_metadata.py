from __future__ import annotations

import json
from pathlib import Path

from tigrbl_auth.cli.artifacts import build_openapi_contract, deployment_from_options


ROOT = Path(__file__).resolve().parents[3]


def test_rfc9728_protected_resource_metadata_surface_is_published() -> None:
    deployment = deployment_from_options(profile="production")
    openapi = build_openapi_contract(deployment, version="0.0.0-test")
    metadata = json.loads((ROOT / "specs" / "discovery" / "profiles" / "production" / "oauth-protected-resource.json").read_text(encoding="utf-8"))

    assert "/.well-known/oauth-protected-resource" in deployment.active_routes
    assert "/.well-known/oauth-protected-resource" in openapi["paths"]
    assert metadata["resource"]
    assert metadata["authorization_servers"]
