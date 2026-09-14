# KCA-ELS Compact Response v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Scope:** AI interaction efficiency and continuity  
**Authority:** Subordinate to PGKI, KCA, and ELS

## 1. Purpose

Define a compact response protocol that reduces conversational overhead without reducing evidence, rigor, traceability, or required decision detail.

## 2. Mandatory response state

For project-engineering turns, prefer the following compact structure:

```text
STATE
EVIDENCE
BLOCKER / RISK
DECISION STATUS
NEXT AUTHORIZED ACTION
```

Fields may be omitted only when genuinely not applicable.

## 3. Compression rules

1. Lead with the current engineering state or action.
2. Avoid generic introductions and repeated project history.
3. Prefer references to already-established artifacts over reproducing their contents.
4. State only facts supported by available evidence.
5. Preserve material caveats and limitations.
6. End with one concrete next authorized action when continuation is possible.
7. Do not use brevity to conceal unresolved findings.
8. Do not cap evidence lists when completeness is required by the contract.
9. Do not summarize away distinctions between FACT, EVIDENCE, INFERENCE, UNKNOWN, CONFLICT, or PROPOSAL.
10. When a task is L2 or higher, retain the information needed to reproduce the reasoning boundary.

## 4. Context reset

At the beginning of a new session, the response protocol should rely on the current bootstrap/checkpoint rather than assuming conversational memory.

Minimum reset state:
- project identity;
- canonical state reference;
- active iteration;
- current objective;
- authorized action;
- blockers/conflicts;
- relevant artifact identifiers.

## 5. Evidence-preservation rule

Compactness is a presentation property, not an evidence policy.

The following are prohibited:
- omitting a blocking finding because it is verbose;
- replacing primary evidence with unsupported summaries;
- treating prior assistant statements as evidence;
- claiming verification when the underlying artifact was not inspected.

## 6. Relationship to external compact-response skills

External skills such as `i-have-adhd` may be evaluated as UX/presentation inputs. Their rules are not authoritative and must not override PGKI/KCA/ELS, contract completeness, evidence requirements, or safety controls.

## 7. Operational status

This document is a proposed project-specific policy. It does not claim automatic enforcement by ChatGPT, an IDE, or an agent runtime.
