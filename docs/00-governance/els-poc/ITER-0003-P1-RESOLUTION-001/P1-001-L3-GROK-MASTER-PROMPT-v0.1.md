# P1-001 L3 External Audit — Master Prompt for Grok v0.1

## ROLE

Act as an independent external forensic auditor for the repository:

https://github.com/GiacoPc/Profesor-Eficiente

You are performing an L3 audit of P1-001.

You have no access to the project's conversational history. Treat this prompt and the supplied L3 audit packet as your complete context. Do not rely on unstated assumptions, prior discussions, or conclusions from other AI systems.

Your task is to determine what the supplied evidence actually establishes under the governing contract.

## INPUT

Primary evidence package:

`P1-001-L3-EXTERNAL-AUDIT-PACKET-v0.1.md`

Packet blob SHA-256:

`1bbe5f35020681891bdd40ebe096ad2d76dc8c2b`

Repository:

https://github.com/GiacoPc/Profesor-Eficiente

Packet branch:

`audit/l3-p1-001-external-packet-001`

You may inspect the repository only to verify facts explicitly relevant to P1-001. Do not modify anything.

## INDEPENDENCE RULES

Do NOT:
- use project chat history;
- assume previous L1/L2 conclusions are correct;
- infer what result the project team wants;
- treat an assertion in the packet as proof when the cited evidence does not support it;
- authorize continuation or closure;
- modify repository files.

The packet is evidence, not authority beyond the governing contract reproduced in it.

## GOVERNING DECISION RULE

For each criterion P1-001-A through P1-001-E, return exactly one of:

- PASS
- FAIL
- UNKNOWN
- CONFLICT

Do not invent intermediate states.

If evidence is absent or inconclusive, use UNKNOWN.
If authoritative evidence disagrees, use CONFLICT.
Do not convert a bounded test into a broader failure class.

## CRITICAL DISTINCTIONS

Preserve these distinctions:

1. Workflow source commit vs. engineering HEAD observed inside a pull-request merge checkout.
2. Current documentary corrections vs. historical execution evidence.
3. Explicitly supported write boundary WB-001 vs. WB-002 through WB-005, which are not established as supported.
4. POSIX process interruption/SIGTERM vs. workstation crash, power loss, Android process death.
5. Schema validation vs. proof of substantive recovery semantics.
6. CI success vs. proof of only the properties actually exercised by that run.

## AUDIT METHOD

For each criterion:

1. Quote or identify the exact contract requirement.
2. Identify the exact supplied evidence.
3. Test whether the evidence satisfies every part of the requirement.
4. Record the evidence boundary.
5. Identify missing evidence or contradictions.
6. Assign PASS / FAIL / UNKNOWN / CONFLICT.

Then independently assess whether all closure prerequisites in the governing contract are satisfied.

Do not infer closure merely because A-E appear to pass. Check the contract's additional closure gates.

## SPECIAL CHECKS

### P1-001-A
Verify that the machine-readable test specification itself contains the exact repository identity required by the contract. Do not substitute another document unless the contract permits it.

### P1-001-B
Verify that controller and target are distinct, identities are recorded, the interruption is actually executed, and the persisted artifact is checked. Keep the claim bounded to the demonstrated process-level interruption.

### P1-001-C
Verify:
- the exact supported boundary being exercised;
- deterministic partial-write interruption;
- persisted artifact identity;
- expected artifact identity;
- deterministic oracle;
- schema compatibility with the oracle result.

Do not promote UNKNOWN boundaries into supported boundaries.

### P1-001-D
Check whether the evidence improperly claims workstation crash, power loss, or Android process death. If these were not actually executed, they must remain non-claims.

### P1-001-E
Check whether quota exhaustion is correctly distinguished from synthetic budget exhaustion. Do not treat a synthetic test as real provider/IDE quota evidence.

## REQUIRED OUTPUT

Return a forensic report in this exact structure:

# P1-001 L3 Independent External Audit

Auditor: Grok
Audit date/time: [UTC]
Repository: [exact repository]
Input packet: P1-001-L3-EXTERNAL-AUDIT-PACKET-v0.1.md
Input packet SHA-256: 1bbe5f35020681891bdd40ebe096ad2d76dc8c2b

## Independence declaration
State whether you performed this review without access to the project's conversational history and without relying on prior audit conclusions.

## Criterion results

### P1-001-A
Result: PASS / FAIL / UNKNOWN / CONFLICT
Evidence:
Evidence boundary:
Missing/contradictory requirement:

### P1-001-B
Result: PASS / FAIL / UNKNOWN / CONFLICT
Evidence:
Evidence boundary:
Missing/contradictory requirement:

### P1-001-C
Result: PASS / FAIL / UNKNOWN / CONFLICT
Evidence:
Evidence boundary:
Missing/contradictory requirement:

### P1-001-D
Result: PASS / FAIL / UNKNOWN / CONFLICT
Evidence:
Evidence boundary:
Missing/contradictory requirement:

### P1-001-E
Result: PASS / FAIL / UNKNOWN / CONFLICT
Evidence:
Evidence boundary:
Missing/contradictory requirement:

## Contract-level closure assessment

State whether the supplied evidence satisfies the governing contract's closure prerequisites.

Use exactly one:
- CLOSURE PREREQUISITES SATISFIED
- CLOSURE PREREQUISITES NOT SATISFIED
- CLOSURE PREREQUISITES UNKNOWN

Explain each blocking or satisfied prerequisite.

## Contradictions and anomalies

List every material contradiction, schema defect, provenance issue, or ambiguity you found.

If none, explicitly state: "No material contradiction identified."

## Evidence boundaries / non-claims

List the claims that the evidence does NOT establish.

## Missing evidence

List the concrete evidence that would be required to resolve any UNKNOWN, FAIL, or CONFLICT result.

## Final factual conclusion

Give a concise factual conclusion only. Do not recommend a political, product, project-management, or architectural choice. Do not authorize continuation.

## Important

Your report is an independent evidence source. It does not itself authorize repository changes, P1-001 closure, or continuation.
