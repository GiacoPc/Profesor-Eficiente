# ELS SECONDARY AUDIT PACK v1.0

**Status:** PREPARED — INTEGRITY REVIEW REQUIRED BEFORE EXTERNAL AUDIT
**Purpose:** Independent external red-team audit of ELS continuity and checkpoint controls.
**Evidence baseline:** `a1f3344c9309dc8051114b67831ce83f44604f65`
**Evidence baseline branch:** `recovery/els-poc-002G`
**Audit pack branch:** `audit/els-secondary-v1.0`

## Independence
The external auditor must not use the primary conversation as evidence. A genuinely independent model/provider or independent execution context is required. The auditor must not modify the repository or silently repair findings.

## Audit scope
The audit covers only evidence that existed on the frozen baseline above, specifically ELS-CHECKPOINT v0.2, POC-002E, POC-002F, POC-002G, the checkpoint verifier, associated tests/evidence, and the claims explicitly bounded by those artifacts.

## Important boundary
The pack does not assert that ELS is production-ready. It is designed to determine whether the available evidence justifies any promotion and to identify defects, false positives, bypasses, contradictions, and missing evidence.

## How to use
1. Give the external auditor `AUDIT-PROMPT.md`.
2. Give it `EVIDENCE-MANIFEST.yaml` and `CLAIM-EVIDENCE-MATRIX.yaml`.
3. Provide the referenced repository files/evidence read-only, either from this repository or as immutable copies.
4. Require the auditor to return a structured verdict using the mandatory format in the prompt.
5. Preserve the returned audit unchanged as external evidence. Do not edit it before reconciliation.
