# Tier 4 External Evidence Checklist

- peer_profile: `ops-cli`
- counterpart_id: `ops-cli-harness`
- required_targets: `OpenAPI 3.1 / 3.2 compatible public contract, OpenRPC 1.4.x admin/control-plane contract, CLI operator surface, Bootstrap and migration lifecycle, Key lifecycle and JWKS publication, Import/export portability, Release bundle and signature verification`
- scenario_ids: `cli-surface, bootstrap-migration, release-bundle-signing, contract-export-verify, operator-lifecycle-roundtrip`
- required_identity_fields: `peer_name, peer_version`
- required_global_identity_fields: `peer_operator`
- required_container_fields: `image_ref, image_digest`
- expected_execution_style: `black-box-cli`
- required_attestation_fields: `attesting_organization, attesting_contact, attestation_timestamp, package_team_member=false, repository_fixture_generated=false`
- required_artifacts: `stdout.log, result.yaml`

## Submission steps

1. Copy `manifest.template.yaml` to `manifest.yaml` and fill every REQUIRED field.
2. Copy `result.template.yaml` to `result.yaml` or emit `result.json` from the independent harness.
3. Replace every placeholder under `required-artifact-placeholders/` with the real preserved artifacts at the exact paths listed in the manifest/counterpart requirements.
4. Add `reproduction.md` if the reproduction notes are not embedded in `manifest.yaml`.
5. Materialize and validate with `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root> --require-full-boundary`.
6. Repository-staged fixtures under `dist/tier4-external-root-fixtures/` are intentionally non-qualifying and will be rejected for Tier 4 promotion.
