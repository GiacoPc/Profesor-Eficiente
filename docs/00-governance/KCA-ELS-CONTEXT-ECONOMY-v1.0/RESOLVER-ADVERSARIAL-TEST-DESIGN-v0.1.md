# Resolver Adversarial Test Design v0.1

Status: PROPOSED_TEST_DESIGN

Tests are designed before any behavioral modification.

- RAT-001: missing core source must yield BLOCKED/UNKNOWN.
- RAT-002: empty objective must yield BLOCKED/CEC-VAL-001.
- RAT-003: non-positive limit must yield BLOCKED/CEC-VAL-002.
- RAT-004: empty selection must not yield a valid-looking package.
- RAT-005: missing dependency must yield a blocking UNKNOWN.
- RAT-006: missing path/hash provenance must yield BLOCKED.
- RAT-007: conflicting source identity must yield blocking CONFLICT.
- RAT-008: blocking conditions must prevent governed continuation.
- RAT-009: F21 integrations must require an explicit target ref; resolver must remain read-only.
- RAT-010: identical source state and objective must yield equivalent source identities.
- RAT-011: output must remain derived and must not claim governance approval.
- RAT-012: keyword scoring must not elevate unrelated artifacts to authority.

A test is passed only after execution and evidence capture. Unexpected results are blocking until reconciled.

This design does not establish correction, criterion closure, or independent L2 validation.
