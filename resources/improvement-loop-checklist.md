# Improvement Loop Checklist

Use this before allowing evidence from one run to change future system behavior.

## Baseline

- [ ] The current harness or workflow has a versioned identity.
- [ ] The intended outcome and evaluation claim are explicit.
- [ ] The current eval suite and known limitations are preserved.
- [ ] Required authority and privacy boundaries are documented.

## Evidence

- [ ] The failure or opportunity is supported by a trace, artifact, check, or review.
- [ ] Sensitive inputs are excluded, minimized, or protected under an explicit retention policy.
- [ ] Evidence provenance is retained.
- [ ] `FAIL`, `ERROR`, `INCOMPLETE`, and `unknown` are not collapsed into success.

## Diagnosis

- [ ] The finding is classified as contract, enforcement, capability, observability, eval, environment, or one-off failure.
- [ ] The proposed change addresses the evidenced cause rather than only its wording.
- [ ] A counter-hypothesis or disconfirming check has been considered.
- [ ] A private incident has been generalized before becoming reusable guidance.

## Candidate

- [ ] The candidate is isolated from the promoted harness.
- [ ] The change is attributable and reviewable.
- [ ] Existing regression cases and the new case are run comparably.
- [ ] Counter-metrics cover quality, cost, latency, privilege, and data exposure where relevant.
- [ ] Generated tests are not treated as independent acceptance.

## Promotion

- [ ] Required deterministic gates pass.
- [ ] Consequential subjective claims receive human or appropriately independent review.
- [ ] Permission, tool, and data-access changes are reviewed separately.
- [ ] Promotion authority is explicit.
- [ ] A rollback path is tested or credibly available.
- [ ] Rejected candidates and failed evidence remain visible.

## After Promotion

- [ ] Later runs are monitored for regression or drift.
- [ ] The change is reusable without repasting private context.
- [ ] The system records which version produced each outcome.
- [ ] The next review point is based on risk or evidence, not arbitrary automation.
