
# Waivers

Waivers are explicit, time-bounded exceptions.

## Rules

- Waivers must be recorded in `register.yaml`.
- Waivers may not widen the certified boundary.
- Waivers may not reclassify an extension target as core.
- Waivers must include approver, rationale, linked issue, and expiry.
- Expired waivers fail release gating.
