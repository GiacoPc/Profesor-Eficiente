# Change Classification Policy

## Purpose

Prevent an AI or developer from deciding subjectively whether a change is significant enough to require an ADR.

## Classification

| Class | Examples | ADR | Additional control |
|---|---|---:|---|
| TRIVIAL | spelling, formatting, comments with no semantic effect | No | CI |
| LOCAL | isolated implementation/documentation change with no contract or invariant impact | Usually no | tests/CI |
| ARCHITECTURAL | module boundary, runtime, data flow, model integration, concurrency, persistence, security boundary | Yes | ADR + tests/evidence |
| GOVERNANCE | Source of Truth, context routing, approval rules, branch/CI policy, invariants | Yes | ADR + governance CI |
| INVARIANT-BREAKING | change to an approved invariant, authority boundary, offline requirement, portability rule, or safety/security invariant | Yes | explicit human approval + evidence |

## Mandatory stop conditions

The agent MUST stop and request an ADR when a change could affect:

- pedagogical authority;
- curriculum authority or MCER constraints;
- mastery/progression gates;
- Student Digital Twin semantics;
- APE responsibilities;
- Formal Domain Model contracts;
- LLM/provider replaceability;
- offline-first guarantees;
- privacy/security boundaries;
- persistent learner data semantics;
- task-routed context rules;
- repository Source of Truth;
- CI governance invariants;
- hardware/runtime architecture;
- public APIs or inter-module contracts.

If classification is ambiguous, classify upward to the more restrictive category.

## Evidence rule

An ADR records a decision. Tests, benchmarks, documents, or other artifacts record evidence. Neither substitutes for the other.
