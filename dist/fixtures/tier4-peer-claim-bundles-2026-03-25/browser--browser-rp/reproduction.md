# Reproduction

1. Use the staged external-root fixture directory `dist/tier4-external-root-fixtures/2026-03-25/browser`.
2. Verify the counterpart metadata for `browser-rp` and inspect the preserved artifacts.
3. Re-run `python scripts/materialize_tier4_peer_evidence.py --external-root dist/tier4-external-root-fixtures/2026-03-25` to normalize the bundle.
4. Cross-check the normalized bundle hashes and the copied peer-artifacts tree.
