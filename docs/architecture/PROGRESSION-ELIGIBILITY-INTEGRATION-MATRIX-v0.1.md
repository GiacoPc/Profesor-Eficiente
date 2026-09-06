# C-007 / C-008 — Progression Eligibility Integration Matrix

**Version:** 0.1-draft  
**Status:** PROPOSED / REQUIRES APPROVAL

## Canonical distinction

```text
ProgressionEligibility = authoritative domain result
APE.PROGRESS          = pedagogical action
```

They must never be represented as the same concept.

## Cross-document integration

| Artifact | Owns / consumes | Must not do |
|---|---|---|
| Curriculum | Defines valid objectives, lessons and mandatory prerequisites | Be rewritten by APE/LLM |
| MasteryPolicy | Defines mastery requirements | Be replaced by local thresholds |
| CLM | Interprets accepted evidence into learning state | Authorize progression action |
| FDM | Evaluates/enforces domain eligibility and transition invariants | Accept an invalid PROGRESS command |
| SDT | Represents current governed learner state | Declare eligibility independently |
| APE | Chooses pedagogical action after eligibility evaluation | Override hard eligibility gates |
| LPH | Supplies/validates bounded linguistic candidates | Authorize progression |
| LLM | Generates candidate content/interpretation | Decide mastery or progression |

## Authority tests

- **P78-AUTH-01:** APE cannot redefine `ProgressionEligibility`.
- **P78-AUTH-02:** LLM cannot establish eligibility.
- **P78-AUTH-03:** SDT cannot independently declare progression eligibility.
- **P78-AUTH-04:** LPH cannot waive mastery/prerequisite gates.
- **P78-AUTH-05:** FDM/domain validation rejects `PROGRESS` when a mandatory hard gate fails.

## Gate tests

- **P78-G01:** `ELIGIBLE` is required for authoritative `PROGRESS`.
- **P78-G02:** mandatory prerequisites must be satisfied.
- **P78-G03:** applicable mastery gates must be satisfied.
- **P78-G04:** evidence must be sufficient for the required mastery claims.
- **P78-G05:** MasteryPolicy identity/version must be valid and attributable.
- **P78-G06:** blocking conflict prevents progression.
- **P78-G07:** stale/incompatible state invalidates the eligibility result.
- **P78-G08:** transition must be valid for the current curriculum state.

## Behavioral tests

- **P78-B01:** `INELIGIBLE` → no authoritative `PROGRESS`.
- **P78-B02:** `INSUFFICIENT_EVIDENCE` → no authoritative `PROGRESS`.
- **P78-B03:** `CONFLICT` → no authoritative `PROGRESS`.
- **P78-B04:** system failure obtaining evidence → controlled insufficient/unavailable state, not fabricated learner failure.
- **P78-B05:** `ELIGIBLE` does not force APE to progress immediately; APE may consolidate or reassess when permitted by its pedagogical contract.
- **P78-B06:** APE's conversational reasoning cannot waive a mandatory domain gate.

## Concurrency / stale-state tests

```text
Eligibility evaluated at state V
        ↓
state changes to V+1
        ↓
APE attempts PROGRESS using V
        ↓
FDM detects incompatible version
        ↓
reject / HOLD / re-evaluate
```

Exact transaction mechanism remains pending SRA/data architecture.

## Integration gate

C-007/C-008 are **source-spec integrated** only after PAD, CLM, FDM, APE and SDT contain direct normative references to this contract or an approved equivalent, with executable checks where applicable.

Current status:

**CONTRACT LEVEL RESOLUTION COMPLETE / SOURCE-SPEC INTEGRATION PENDING / AUDIT PENDING.**
