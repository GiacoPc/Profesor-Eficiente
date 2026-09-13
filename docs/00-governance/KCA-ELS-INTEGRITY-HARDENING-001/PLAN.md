# Plan — KCA/ELS Integrity Hardening — Emergency Corrective Iteration

1. Freeze current base identity and preserve the branch lineage.
2. Define the hardening contract before implementation.
3. Define the machine-readable acceptance matrix with explicit blocking semantics.
4. Define the adversarial failure model from the recent integrity incidents.
5. Cross-check contract and matrix for semantic identity.
6. Prepare a bounded independent L2 audit pack; do not reuse a broader prompt whose evidence scope does not match this iteration.
7. Obtain independent audit and reconcile findings against exact repository evidence.
8. Seek human approval.
9. Only after approval, create a separate implementation iteration for validators/control-plane changes.
10. Re-run adversarial tests, then evaluate KCA/ELS operational readiness separately.

## Hard stop

Any contradiction between contract, matrix, context manifest, audit prompt or evidence inventory stops the workflow. No package is sent for substantive external audit until compatibility is verified.
