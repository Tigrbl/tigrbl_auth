# Validated Execution Report

- Passed: `False`

## Summary

- validated_artifact_count: `7`
- out_of_scope_validated_artifact_count: `5`
- required_validated_inventory_count: `30`
- validated_inventory_present_count: `6`
- validated_inventory_complete: `False`
- runtime_matrix_present_count: `0`
- runtime_matrix_expected_count: `14`
- runtime_matrix_passed_count: `0`
- runtime_matrix_green: `False`
- test_lane_expected_count: `15`
- test_lane_passed_count: `0`
- in_scope_test_lanes_green: `False`
- migration_portability_passed: `False`
- tier3_evidence_rebuilt_from_validated_runs: `True`

## Failures

- Validated artifact inventory is below the required 14 runtime + 15 test lanes + 1 migration threshold.
- Validated clean-room runtime matrix is incomplete.
- Validated in-scope certification lane execution is incomplete.
- Migration portability validation across SQLite and PostgreSQL is missing.

## Warnings

- Unsupported-version or out-of-scope validated manifests are present and excluded from certification counts.

## Details

- runtime_matrix_missing: `['base@py3.10', 'base@py3.11', 'base@py3.12', 'sqlite-uvicorn@py3.10', 'sqlite-uvicorn@py3.11', 'sqlite-uvicorn@py3.12', 'postgres-hypercorn@py3.10', 'postgres-hypercorn@py3.11', 'postgres-hypercorn@py3.12', 'tigrcorn@py3.11', 'tigrcorn@py3.12', 'devtest@py3.10', 'devtest@py3.11', 'devtest@py3.12']`
- runtime_matrix_present_count: `0`
- test_lane_missing: `['core@py3.10', 'core@py3.11', 'core@py3.12', 'integration@py3.10', 'integration@py3.11', 'integration@py3.12', 'conformance@py3.10', 'conformance@py3.11', 'conformance@py3.12', 'security-negative@py3.10', 'security-negative@py3.11', 'security-negative@py3.12', 'interop@py3.10', 'interop@py3.11', 'interop@py3.12']`
- test_lane_present_count: `5`
- migration_manifest_present: `True`
- required_validated_inventory_count: `30`
- validated_inventory_present_count: `6`
- validated_inventory_complete: `False`
- runtime_evidence: `{}`
- test_lane_evidence: `{'conformance@py3.11': {'path': 'dist/validated-runs/test-conformance-py311.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 22, 'tests_total': 22}, 'conformance@py3.13': {'path': 'dist/validated-runs/test-conformance-py313.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 22, 'tests_total': 22}, 'core@py3.11': {'path': 'dist/validated-runs/test-core-py311.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 67, 'tests_total': 67}, 'core@py3.13': {'path': 'dist/validated-runs/test-core-py313.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 67, 'tests_total': 67}, 'integration@py3.11': {'path': 'dist/validated-runs/test-integration-py311.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 31, 'tests_total': 31}, 'integration@py3.13': {'path': 'dist/validated-runs/test-integration-py313.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 31, 'tests_total': 31}, 'interop@py3.11': {'path': 'dist/validated-runs/test-interop-py311.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 14, 'tests_total': 14}, 'interop@py3.13': {'path': 'dist/validated-runs/test-interop-py313.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 14, 'tests_total': 14}, 'security-negative@py3.11': {'path': 'dist/validated-runs/test-security-negative-py311.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 1, 'tests_total': 1}, 'security-negative@py3.13': {'path': 'dist/validated-runs/test-security-negative-py313.json', 'manifest_passed': True, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'pytest_report_present': True, 'pytest_exit_code': 0, 'pytest_report_exit_code': 0, 'tests_collected': 1, 'tests_total': 1}}`
- migration_evidence: `[{'path': 'dist/validated-runs/migration-portability-py313.json', 'manifest_passed': False, 'counts_as_passed': False, 'identity': None, 'environment_identity_ready': False, 'install_evidence_ready': False, 'backends': ['sqlite'], 'passed_backends': ['sqlite'], 'expected_head_revision': None, 'downgrade_target_revision': None}]`
- validated_manifests: `['dist/validated-runs/migration-portability-py313.json', 'dist/validated-runs/test-conformance-py311.json', 'dist/validated-runs/test-core-py311.json', 'dist/validated-runs/test-integration-py311.json', 'dist/validated-runs/test-interop-py311.json', 'dist/validated-runs/test-security-negative-py311.json', 'dist/validated-runs/tier3-evidence-py313.json']`
- out_of_scope_validated_manifests: `[{'path': 'dist/validated-runs/test-conformance-py313.json', 'kind': 'test-lane', 'python_version': '3.13', 'identity': 'conformance@py3.13', 'reason': 'test lane is outside the supported certification matrix'}, {'path': 'dist/validated-runs/test-core-py313.json', 'kind': 'test-lane', 'python_version': '3.13', 'identity': 'core@py3.13', 'reason': 'test lane is outside the supported certification matrix'}, {'path': 'dist/validated-runs/test-integration-py313.json', 'kind': 'test-lane', 'python_version': '3.13', 'identity': 'integration@py3.13', 'reason': 'test lane is outside the supported certification matrix'}, {'path': 'dist/validated-runs/test-interop-py313.json', 'kind': 'test-lane', 'python_version': '3.13', 'identity': 'interop@py3.13', 'reason': 'test lane is outside the supported certification matrix'}, {'path': 'dist/validated-runs/test-security-negative-py313.json', 'kind': 'test-lane', 'python_version': '3.13', 'identity': 'security-negative@py3.13', 'reason': 'test lane is outside the supported certification matrix'}]`
- recognized_manifest_paths: `['dist/validated-runs/migration-portability-py313.json', 'dist/validated-runs/test-conformance-py311.json', 'dist/validated-runs/test-conformance-py313.json', 'dist/validated-runs/test-core-py311.json', 'dist/validated-runs/test-core-py313.json', 'dist/validated-runs/test-integration-py311.json', 'dist/validated-runs/test-integration-py313.json', 'dist/validated-runs/test-interop-py311.json', 'dist/validated-runs/test-interop-py313.json', 'dist/validated-runs/test-security-negative-py311.json', 'dist/validated-runs/test-security-negative-py313.json', 'dist/validated-runs/tier3-evidence-py313.json']`
- ignored_json_paths: `[]`
