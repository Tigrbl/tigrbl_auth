# RPC Control Plane

`tigrbl_auth.api.rpc` is the implementation-backed operator/admin RPC plane.

The package now owns:

- the authoritative RPC method registry
- executable handler modules under `methods/`
- request/response schema modules under `schemas/`
- contract metadata used to generate `specs/openrpc/tigrbl_auth.admin.openrpc.json`

OpenRPC generation is intentionally derived from executable method registration,
not from a detached catalog. Any divergence between the committed OpenRPC
artifact and the implementation-backed registry is treated as contract drift.
