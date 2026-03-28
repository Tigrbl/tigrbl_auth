# Reproduction

1. Run the external counterpart `dpop-client` against the `hardening` profile.
2. Capture exact HTTP/RPC transcripts, peer identity, peer version, image reference, immutable image/container digest, scenario results, and reproduction notes.
3. Supply the artifacts under an external root at `<external-root>/dpop/`.
4. Re-run `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root>` to normalize and validate the preserved bundle for `dpop`.
5. Tier 4 promotion occurs only when the counterpart identity, attestation class, scenario coverage, and reproduction requirements are all satisfied.
