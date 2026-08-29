# PGKI-1.1 — High-Impact Gate Matrix

**Status:** PROPOSED HARDENING — PENDING HUMAN APPROVAL
**Purpose:** Define when independent secondary AI review is mandatory. This document does not authorize a gate by itself.

## Mandatory secondary review

| Gate class | Secondary auditor | Mode | Minimum deterministic evidence |
|---|---|---|---|
| P0 governance/integrity | REQUIRED | Red-team | CI + repository refs |
| P0/P1 architecture | REQUIRED | Red-team | Architecture/spec traceability |
| P0/P1 security | REQUIRED | Red-team | Security tests/tool output where applicable |
| P0/P1 hardware/runtime/NPU | REQUIRED | Red-team | Device-specific compatibility evidence + measurements |
| P0/P1 performance/latency/RAM/thermal/energy | REQUIRED | Red-team | Reproducible benchmark results |
| P0/P1 LLM/model/runtime selection | REQUIRED | Red-team | Compatibility + benchmark/evaluation evidence |
| P0/P1 pedagogical authority or progression logic | REQUIRED | Red-team | Specification + pedagogical evidence/evaluation protocol |
| Release/readiness gate | REQUIRED | Independent review | CI + release checklist + required evidence |
| P2/P3 implementation change | OPTIONAL unless escalated | Standard review | Relevant tests |
| Documentation-only typo/formatting | NOT REQUIRED | N/A | CI/document validation if applicable |

## Escalation rule

If the change classification is ambiguous, use the higher-risk class. If evidence is incomplete, the gate remains `UNKNOWN`/`NOT_AVAILABLE` and cannot pass.

## Independence rule

The secondary auditor must receive an immutable audit pack and must not be instructed to confirm the primary conclusion. For P0/P1 gates it should attempt falsification/red-team analysis.

## Gate closure

A critical gate requires:

`deterministic evidence + primary analysis + secondary independent verdict + human decision`

No AI verdict alone closes a critical gate.
