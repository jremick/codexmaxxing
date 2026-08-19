# Improvement Loop Checklist

Use this before allowing evidence from one run to change future behavior.

## Quick Check

For a small, low-risk workflow change, answer five questions:

- [ ] What evidence shows the current workflow has a real problem?
- [ ] Does the proposed change address that problem rather than merely rewording the prompt?
- [ ] Was it compared with the current version using the same important checks?
- [ ] Could it broaden permissions, collect more data, or make another result worse?
- [ ] Can it be reviewed and rolled back?

Use the full checklist below when the workflow is higher-risk, widely shared, or allowed to act with limited supervision.

## Baseline

- [ ] The current harness or workflow has a versioned identity.
- [ ] The intended outcome and evaluation claim are explicit.
- [ ] The current eval suite and known limitations are preserved.
- [ ] Required permission and privacy boundaries are documented.

## Evidence

- [ ] The failure or opportunity is supported by a trace, artifact, check, or review.
- [ ] Sensitive inputs are excluded, minimized, or protected under an explicit retention policy.
- [ ] The source of the evidence is retained.
- [ ] `FAIL`, `ERROR`, `INCOMPLETE`, and `unknown` are not collapsed into success.

## Diagnosis

- [ ] The finding is classified as unclear expectation, enforcement, missing capability, missing evidence, invalid eval, environment, or one-off failure.
- [ ] The proposed change addresses the evidenced cause rather than only its wording.
- [ ] Another plausible explanation or disconfirming check has been considered.
- [ ] A private incident has been generalized before becoming reusable guidance.

## Proposed Version

- [ ] The proposed version is isolated from the current harness.
- [ ] The change is attributable and reviewable.
- [ ] Existing regression cases and the new case are run comparably.
- [ ] Checks cover quality, cost, latency, permissions, and data exposure where relevant.
- [ ] Generated tests are not treated as independent acceptance.

## Adoption

- [ ] Required deterministic gates pass.
- [ ] Consequential subjective claims receive human or appropriately independent review.
- [ ] Permission, tool, and data-access changes are reviewed separately.
- [ ] Permission to adopt the change is explicit.
- [ ] A rollback path is tested or credibly available.
- [ ] Rejected versions and failed evidence remain visible.

## After Adoption

- [ ] Later runs are monitored for regression or drift.
- [ ] The change is reusable without repasting private context.
- [ ] The system records which version produced each outcome.
- [ ] The next review point is based on risk or evidence, not arbitrary automation.
