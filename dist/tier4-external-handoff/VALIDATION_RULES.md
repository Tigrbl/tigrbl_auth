# Tier 4 External Evidence Validation Rules

A preserved external bundle only counts toward strict independent claims when all of the following are true:

- `counterpart_id` matches the declared peer profile counterpart.
- `peer_identity.peer_name`, `peer_identity.peer_version`, and `peer_identity.peer_operator` are present and not placeholder values.
- `peer_runtime.image_ref` and `peer_runtime.image_digest` are present and the digest is immutable (`sha256:...`).
- `peer_runtime.execution_style` matches the expected counterpart execution style.
- `independence_attestation.attestation_class = independent-external`.
- `independence_attestation.attesting_organization`, `attesting_contact`, and `attestation_timestamp` are present.
- `independence_attestation.package_team_member = false`.
- `independence_attestation.repository_fixture_generated = false`.
- repository-staged fixtures, self-attested submissions, and placeholder manifests are rejected fail-closed.
- every required artifact exists and every scenario result is present and passed.
- `source_revision` and reproduction material are preserved.
