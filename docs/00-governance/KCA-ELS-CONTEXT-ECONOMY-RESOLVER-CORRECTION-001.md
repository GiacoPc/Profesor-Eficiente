# KCA-ELS Context Economy — Resolver Correction Iteration 001

**Status:** IMPLEMENTED ON ISOLATED CORRECTION BRANCH / REQUIRES VALIDATION  
**Base:** `19bacd64ef723de9919b0d008d1cd78044821ead`  
**Branch:** `kca/els-context-economy-resolver-correction-001`

## Objective
Correct the resolver's unsafe behavior of emitting an apparently valid package with `blockers: []` without proving that required inputs and repository identity are available.

## Normative changes

1. The resolver is explicitly read-only and cannot authorize governance actions.
2. Empty objectives, invalid limits, missing core artifacts, unavailable repository identity, and absent candidate sources produce `status: BLOCKED`.
3. Blocking diagnostics carry a stable code, state (`FAIL` or `UNKNOWN`), and detail.
4. A successfully constructed package is emitted as `VALIDATION_REQUIRED`, not as proof of compliance.
5. The package includes source SHA-256 values and byte counts.
6. The output process returns a non-zero exit code for `BLOCKED`.
7. The resolver's output must still undergo independent relevance, dependency, provenance, continuation-gate, and F21 verification.

## Explicit non-claims

- This iteration does not establish CEC-01…CEC-06 closure.
- It does not implement a complete semantic dependency graph.
- It does not make writes; F21 write controls remain normative requirements for every external writer.
- It does not establish token savings.

## Acceptance focus

- Missing-core-source adversarial test must block.
- Empty-objective test must block.
- Repository-identity failure must block.
- Normal resolution must return `VALIDATION_REQUIRED` and an explicit validation warning.
- No output may describe itself as an authorization or governance proof.
