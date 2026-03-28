# Release Gates

Release gates are policy-as-code manifests.

The current gate order is:

1. `gate-00-structure`
2. `gate-05-governance`
3. `gate-10-static`
4. `gate-12-project-tree-layout`
5. `gate-15-boundary-enforcement`
6. `gate-18-migration-plan`
7. `gate-20-tests`
8. `gate-25-wrapper-hygiene`
9. `gate-30-contracts`
10. `gate-35-contract-sync`
11. `gate-40-evidence`
12. `gate-45-evidence-peer`
13. `gate-50-release-bundle`
14. `gate-55-contract-validation`
15. `gate-60-release-signing`
16. `gate-65-state-reports`
17. `gate-75-test-classification`
18. `gate-85-peer-profiles`
19. `gate-90-release`
20. `gate-95-recertification`

A later gate may assume the earlier gates already passed.
