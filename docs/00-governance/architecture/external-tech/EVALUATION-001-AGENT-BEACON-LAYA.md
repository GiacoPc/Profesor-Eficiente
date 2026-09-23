# External Technology Evaluation 001 — Agent Beacon / Laya

**Status:** EVALUATED / NO INTEGRATION AUTHORIZED
**Scope:** Architectural investigation only
**Project:** Profesor-Eficiente
**Date:** 2026-09-23

## 1. Purpose

Record the architectural evaluation of two external repositories requested for investigation:

- Agent Beacon — Asymptote Labs
- Laya — NandhaKishorM

This record is intentionally documentary. It does not add either project as a product dependency, does not change the pedagogical authority model, and does not authorize implementation.

## 2. Agent Beacon

Repository: https://github.com/Asymptote-Labs/agent-beacon
License observed: MIT
Observed current release during evaluation: v1.3.14

### Observed characteristics

Agent Beacon is an open-source telemetry/observability layer for AI-agent runtimes. Its documented architecture centers on normalized runtime events, local collection/processing, durable local JSONL output, local inspection/dashboard capabilities, and integrations with agent runtimes and CI environments.

Its event model distinguishes observed versus inferred fidelity and provides structured event identity/provenance concepts.

### Architectural relevance

Relevant ideas for Profesor-Eficiente:

1. Normalized event schema for AI/runtime events.
2. Explicit provenance and fidelity separation.
3. Durable local event history.
4. Local-first observability.
5. Structured evidence suitable for forensic audit.

### Integration assessment

**DECISION: ADOPT IDEAS / DO NOT INTEGRATE WHOLE PRODUCT**

Rationale:

- Agent Beacon is principally an observability/security telemetry layer, not a pedagogical runtime.
- No verified Android-native integration path was established during this evaluation.
- Its CLI/Go/OpenTelemetry/dashboard/SIEM-oriented footprint would introduce unnecessary runtime and operational surface for the current Android offline-first scope.
- Direct adoption would risk coupling the product runtime to infrastructure that is not required for pedagogical execution.

Potential future use is limited to architecture patterns or a narrowly scoped adapter if a concrete requirement emerges.

## 3. Laya

Repository: https://github.com/NandhaKishorM/laya
License observed: Apache-2.0

### Observed characteristics

Laya is documented as a multilingual, non-autoregressive typed decision engine. Its primitives include choice, score, and probability-style decisions, with confidence information and routing workflows.

The repository documents English and multilingual checkpoints, Python/PyTorch/Transformers/Hugging Face dependencies, CPU/GPU latency measurements, and confidence gating patterns.

The repository also documents important limitations: base checkpoints are near the stated benchmark's random/majority baselines without fine-tuning; high-cardinality choices degrade; some primitives are weak; language coverage is asymmetric; and fine-tuning is a major part of the intended value.

### Architectural relevance

Potential fit as an auxiliary decision component for the Adaptive Pedagogical Engine (APE):

- learner-error classification;
- pedagogical-action classification;
- mastery-state classification;
- weakness prioritization;
- confidence-gated routing.

### Authority constraint

Laya must not become the pedagogical authority.

The authoritative layers remain the approved pedagogical/domain artifacts and APE policy:

**MCER/PAD/CLM/FDM -> pedagogical policy/APE -> model-assisted decisions**

A learned classifier may propose or classify; it must not override formal pedagogical constraints.

### Integration assessment

**DECISION: RESEARCH / PROTOTYPE CANDIDATE / DO NOT INTEGRATE YET**

Before any integration consideration, the following evidence would be required:

1. A representative Spanish-speaking English-learner evaluation dataset.
2. Task-specific metrics for each proposed decision.
3. Calibration/confidence analysis.
4. False-positive/false-negative analysis for pedagogically consequential decisions.
5. Comparison against deterministic rules and the existing LLM/APE path.
6. Android deployment feasibility using an explicitly selected runtime/format.
7. Memory, latency, thermal, battery, and offline behavior measurements on the declared target hardware.
8. Failure-mode analysis demonstrating fail-closed behavior.
9. APE authority tests proving that model output cannot bypass pedagogical policy.

No such production-grade evidence is currently established by this evaluation.

## 4. Combined architectural implication

The two repositories suggest a useful separation of concerns, but this is an architectural proposal, not an approved implementation:

**Generative intelligence**
- LLM for dialogue, explanation, generation and contextual reasoning.

**Decision intelligence**
- Small/structured models or deterministic classifiers for bounded classification, routing and confidence estimation.

**Pedagogical authority**
- Formal MCER/PAD/CLM/FDM constraints and APE policy.

**Observability/provenance**
- Normalized local events, explicit evidence fidelity, and durable audit records.

The separation is consistent with the already approved direction that pedagogical authority must remain outside the LLM.

## 5. Current decision matrix

| Candidate | Current disposition | Product dependency | Further evidence required |
|---|---|---:|---|
| Agent Beacon | Adopt selected architectural ideas only | NO | Only if a concrete observability requirement justifies an adapter |
| Laya | Research/prototype candidate | NO | YES — task evaluation + mobile deployment + APE authority tests |

## 6. Explicit non-actions

This evaluation:

- does not add Agent Beacon as a dependency;
- does not add Laya as a dependency;
- does not modify Android/Kotlin/Rust production code;
- does not replace or select an LLM;
- does not modify PAD, CLM, FDM or APE authority;
- does not modify P1-001 evidence or its oracle;
- does not modify P1-002, P1-003, P1-004 or P1-005;
- does not authorize continuation of the ELS sequence;
- does not close P1-001;
- does not declare ELS operational readiness.

## 7. Provenance and confidence

**FACT:** The repositories and their documented characteristics were inspected during the external technology investigation.

**INFERENCE/PROPOSAL:** The architectural separation described in section 4 may improve modularity and governance.

**UNKNOWN:** Android production feasibility for either project was not established by this record.

**UNKNOWN:** Whether Laya would improve pedagogical decision quality on this project's real learner population.

**UNKNOWN:** Whether Agent Beacon would provide enough product value to justify any Android adapter.

No claim of production suitability is made.

## 8. Result

External technology evaluation completed.

**Agent Beacon:** ADOPT IDEAS / DO NOT INTEGRATE WHOLE PRODUCT.

**Laya:** RESEARCH / PROTOTYPE CANDIDATE / DO NOT INTEGRATE YET.

The next admissible step remains the independent L2 review of P1-001, not implementation of either external repository.
