# C-010 LLMGenerationCandidate Integration Matrix — v0.1

**Status:** PROPOSED / REQUIRES APPROVAL
**Purpose:** Cross-document integration and authority checks for the LLMGenerationCandidate lifecycle.

## 1. Canonical contract

Primary contract: `docs/architecture/LLM-GENERATION-CANDIDATE-LIFECYCLE-v0.1.md`.

## 2. Responsibility matrix

| Area | Authoritative responsibility | C-010 boundary |
|---|---|---|
| Curriculum | Curriculum authority | Candidate cannot mutate curriculum |
| CLM | Learning-state semantics | Candidate cannot directly mutate learning state |
| FDM | Domain invariants and authoritative mutations | Candidate must pass governed domain path before authoritative state changes |
| SDT | Learner-state projection | Candidate cannot write SDT directly |
| APE | Pedagogical decision | Candidate executes a bounded decision; it cannot create the decision authority |
| LPH | Linguistic/interaction constraints and validation | Candidate validation and bounded interpretation |
| LLM Gateway | Capability abstraction | Produces non-authoritative candidate |
| LLM | Probabilistic generation | No domain authority |
| MasteryPolicy | Mastery requirements | Candidate cannot define or override policy |
| Evidence/Assessment | Authoritative evidence/evaluation contracts | Candidate contribution requires a separate governed record/path |

## 3. Critical distinctions

```text
GenerationCandidate ≠ learner evidence
GenerationCandidate ≠ assessment
GenerationCandidate ≠ mastery
GenerationCandidate ≠ progression eligibility
GenerationCandidate ≠ SDT state
Validation pass ≠ domain authority
Acceptance for one use ≠ blanket trust
LLM confidence ≠ evidence certainty
```

## 4. Authority tests

- **C010-AUTH-01:** no direct candidate → authoritative domain mutation.
- **C010-AUTH-02:** candidate cannot redefine MasteryPolicy.
- **C010-AUTH-03:** candidate cannot establish ProgressionEligibility.
- **C010-AUTH-04:** candidate cannot write authoritative SDT state.
- **C010-AUTH-05:** candidate error/mastery/readiness claims remain non-authoritative until the relevant evidence/assessment contract is independently satisfied.
- **C010-AUTH-06:** scoped acceptance cannot be reused as blanket authority for another purpose.

## 5. Validation tests

- **C010-VAL-01:** malformed candidate is rejected or safely repaired/regenerated.
- **C010-VAL-02:** curriculum/objective mismatch is rejected.
- **C010-VAL-03:** unsupported or prohibited output is rejected.
- **C010-VAL-04:** required uncertainty is preserved.
- **C010-VAL-05:** validation provenance is recorded where persistence is required.

## 6. Lifecycle tests

- **C010-LIFE-01:** every persisted candidate has stable identity and request provenance.
- **C010-LIFE-02:** rejection is terminal for that candidate instance.
- **C010-LIFE-03:** repair/regeneration creates a new candidate identity.
- **C010-LIFE-04:** lineage to a prior candidate is preserved where applicable.
- **C010-LIFE-05:** historical candidate content is not silently rewritten.

## 7. Model and offline tests

- **C010-MODEL-01:** replacing the LLM does not alter domain gates.
- **C010-MODEL-02:** removing the LLM cannot permit invalid mastery or progression.
- **C010-OFF-01:** LLM unavailability produces a controlled fallback/capability-unavailable state.
- **C010-OFF-02:** LLM failure cannot become learner failure.

## 8. Assessment conversion gate

When a candidate legitimately contributes to assessment:

```text
Candidate
   ↓
explicit conversion/assessment contract
   ↓
separate Evidence/Assessment record
   ↓
policy/domain validation
   ↓
authoritative state if all gates pass
```

The conversion must preserve provenance. Candidate text cannot be treated as raw learner observation merely because the LLM produced an assessment-like structure.

## 9. Integration gate

C-010 is **CONTRACT-LEVEL INTEGRATED** when the lifecycle contract and this matrix are reviewed against PAD, CLM, FDM, APE, LPH and SDT, and the source specifications contain explicit compatible boundaries.

It is **not APPROVED** until automated checks, independent secondary audit and human approval are complete.

Current status: **CONTRACT LEVEL / SOURCE-SPEC + AUTOMATION + AUDIT GATES PENDING**.
