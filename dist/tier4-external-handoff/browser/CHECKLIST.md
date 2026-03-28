# Tier 4 External Evidence Checklist

- peer_profile: `browser`
- counterpart_id: `browser-rp`
- required_targets: `RFC 6749, RFC 7636, RFC 7516, RFC 8414, RFC 8615, RFC 9207, OIDC Core 1.0, OIDC Discovery 1.0, OIDC UserInfo`
- scenario_ids: `browser-authz-code, browser-oidc-discovery, browser-userinfo, browser-jwe-id-token, browser-issuer-parameter, browser-hardening-discovery-truthfulness`
- required_identity_fields: `peer_name, peer_version`
- required_global_identity_fields: `peer_operator`
- required_container_fields: `image_ref, image_digest`
- expected_execution_style: `black-box-browser`
- required_attestation_fields: `attesting_organization, attesting_contact, attestation_timestamp, package_team_member=false, repository_fixture_generated=false`
- required_artifacts: `http-transcript.yaml, browser-trace.json, result.yaml`

## Submission steps

1. Copy `manifest.template.yaml` to `manifest.yaml` and fill every REQUIRED field.
2. Copy `result.template.yaml` to `result.yaml` or emit `result.json` from the independent harness.
3. Replace every placeholder under `required-artifact-placeholders/` with the real preserved artifacts at the exact paths listed in the manifest/counterpart requirements.
4. Add `reproduction.md` if the reproduction notes are not embedded in `manifest.yaml`.
5. Materialize and validate with `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root> --require-full-boundary`.
6. Repository-staged fixtures under `dist/tier4-external-root-fixtures/` are intentionally non-qualifying and will be rejected for Tier 4 promotion.
