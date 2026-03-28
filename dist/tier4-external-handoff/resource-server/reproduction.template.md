# Reproduction

1. Identify the independent external counterpart `resource-server` and the operator who ran it.
2. Capture the exact commands, image/container digest, runtime details, and environment used for peer profile `resource-server`.
3. Preserve the exact HTTP/RPC/browser transcripts and all profile-specific artifacts.
4. Record enough detail for a third party to reproduce the run without access to repository-local fixtures.
5. Materialize with `python scripts/materialize_tier4_peer_evidence.py --external-root <external-root> --require-full-boundary`.
