# Final Release Gate Report

- Passed: `False`

## Summary

- runtime_profiles_truly_ready: `False`
- validated_inventory_complete: `False`
- required_validated_inventory_count: `30`
- validated_inventory_present_count: `6`
- clean_room_install_matrix_green: `False`
- in_scope_test_lanes_green: `False`
- migration_portability_passed: `False`
- tier3_evidence_rebuilt_from_validated_runs: `True`
- tier4_bundle_promotion_complete: `False`

## Failures

- Runtime profiles are not all ready in the preserved validated-run inventory.
- At least one kept runner is still missing.
- Validated artifact inventory is below the required 14 runtime + 15 test lanes + 1 migration threshold.
- The clean-room install matrix is not green from validated-run evidence.
- In-scope certification test lanes are not green from validated-run evidence.
- Migration portability validation is not preserved for both SQLite and PostgreSQL.

## Warnings

- Tier 4 bundle promotion is not complete for the retained boundary.
