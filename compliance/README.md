# Compliance Plane

This directory is the package governance plane.

## Subdirectories

- `targets/` — declared standards, profiles, target buckets, surfaces, boundaries, and label corrections
- `mappings/` — traceability between targets, flags, modules, surfaces, contracts,
  gates, and ADRs
- `claims/` — declared claim tiers, promotion policy, repository state, and
  release intent
- `evidence/` — preserved evidence-bundle manifests and retention policy
- `gates/` — release-gate policy as code
- `waivers/` — explicit, time-bounded, reviewable exceptions only

## Rule

A target is not certifiable unless it is:
1. declared in `targets/`,
2. mapped in `mappings/`,
3. claimed in `claims/`,
4. evidenced under `evidence/`,
5. release-gated under `gates/`,
6. and not hidden behind an undocumented waiver.
