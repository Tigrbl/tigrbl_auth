# External Interop and Tier 4 Promotion

1. Run the independent external counterpart defined in `compliance/evidence/peer_counterparts/<id>.yaml`.
2. Capture exact HTTP/RPC transcripts, peer identity, peer version, peer operator, image reference, immutable image/container digest, scenario results, and reproduction notes.
3. Place the artifacts under `<external-root>/<peer-profile>/` with at least `manifest.yaml` and `result.yaml` (or `result.json`).
4. Ensure `manifest.yaml` declares `counterpart_id`, `peer_identity`, `peer_runtime`, and `independence_attestation.attestation_class=independent-external`, plus explicit attesting organization/contact/timestamp metadata and `package_team_member=false`.
5. Execute `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root> --require-full-boundary`.
6. Review `docs/compliance/PEER_MATRIX_REPORT.md`, `docs/compliance/TIER4_PROMOTION_MATRIX.md`, and `docs/compliance/current_state_report.md`.
7. Repository-staged fixture roots under `dist/tier4-external-root-fixtures/` are for fail-closed pipeline testing only and never qualify for strict independent claims.
8. Review the remaining validated runtime/test/migration gates before making final package-level certification claims.
