# Independent L2 Audit Prompt — Correction 002

Audit the correction contract for KCA/ELS Integrity Hardening 002 independently and adversarially.

Baseline target branch: `kca/els-integrity-hardening-002-correction`
Audit scope is limited to the correction contract, acceptance matrix, self-audit, reconciliation, and their direct semantic relationships.

Audit P1-F21 as a first-class normative control: explicit target declaration, resolution, pre-write HEAD verification, explicit target write, post-write re-fetch, and result verification. Determine whether omission or implicit target is a blocking failure and whether alternate write surfaces are covered.

Audit P1-C01-C06 for one-to-one independently testable acceptance criteria, including PASS/FAIL/UNKNOWN/CONFLICT, blocking semantics, evidence requirements, and implementation-precondition semantics.

Audit KCAH-011 decomposition into exact package-byte identity, source-state identity, and reproducible package generation.

Red-team Markdown/YAML consistency, scope ambiguity, hidden aggregation, bypasses, and authority leakage.

Use epistemic labels OBSERVED, VERIFIED, INFERRED, UNKNOWN, NOT_AVAILABLE, CONFLICT. Do not treat self-audit claims as proof. Do not authorize implementation, P1 closure, readiness, or autonomy.

Required verdict: PASS | PASS_WITH_LIMITATIONS | FAIL | UNKNOWN | CONFLICT.

Required output: executive verdict, baseline identity, P1-F21 assessment, C01-C06 assessment, KCAH-011 assessment, consistency findings, bypass analysis, evidence gaps, P0-P3 findings, corrective actions, and explicit auditor boundary.
