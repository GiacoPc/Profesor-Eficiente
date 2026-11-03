# P1-001 Acceptance Criteria — Contract v0.2

P1-001 required property: recovery evidence must identify its failure class and evidence boundary and must never promote lower-fidelity simulation to a higher-fidelity claim.

- **P1-001-A:** machine-readable test specification records `failure_class`, `environment`, `interruption_method`, `interruption_point`, `persisted_artifact`, `expected_recovery`, `evidence_boundary`, and exact repository identity.
- **P1-001-B:** at least one independently executed process-interruption test demonstrates durable checkpoint recovery after unexpected process termination; evidence records process identity, interruption method, pre-interruption checkpoint identity, post-interruption recovery result, and exact repository identity; independent means controller distinct from terminated process and both identities recorded.
- **P1-001-C:** partial/interrupted writes are exercised through at least one reproducible test for each supported write boundary; oracle deterministically classifies `RECOVERABLE`, `INVALID`, `CONFLICT`, or `UNKNOWN` using an explicit decision table.
- **P1-001-D:** higher-fidelity claims remain `UNVERIFIED` unless corresponding failure class is actually executed and evidenced; process simulation cannot satisfy higher-fidelity claim by inference.
- **P1-001-E:** quota exhaustion is distinct; synthetic budget exhaustion cannot satisfy real provider/IDE quota claim.

## Closure evidence

Test specification + execution evidence + exact identity + evidence boundary + self-audit + independent L2 review.

Source: `docs/00-governance/els-poc/ITER-0003-P1-RESOLUTION-001/P1-RESOLUTION-CONTRACT-v0.2.md`
Source Git blob SHA observed: `db398fc717d12fdbc37c8b6e4bdcf299245fc8de`
