# Verification Before Completion

The final answer should not be the first time a task becomes precise.

Verification is where Codex stops being a confident narrator and starts being useful.

## Principle

Choose the check that would catch the most likely wrong-but-plausible result.

For a code change, that might be a focused test or build. For a UI change, it might be a browser screenshot across viewports. For documentation, it might be a link check and a quick secret/path scan.

## Verification Ladder

Use the smallest rung that proves the task:

1. Static check: formatting, linting, schema validation, link checking.
2. Unit or focused behavior check.
3. Integration check across the touched boundary.
4. Live read-back or browser inspection.
5. Human review for subjective quality.

Higher is not always better. A live check can be overkill for a typo fix. A static check is too weak for a behavioral change.

## Verify The System As Well As The Output

For a persistent harness or orchestration graph, task completion is only one claim. Also test:

- required state transitions and failure routes;
- architecture, authority, and data-handling invariants;
- recovery after interruption or partial failure;
- candidate behavior against the promoted baseline;
- regression cases derived from prior failures;
- counter-metrics such as cost, latency, privilege growth, or data exposure.

Self-generated tests and agreement among agents can provide evidence, but they are not independent acceptance. Keep deterministic gates outside the model when a hard requirement can be checked mechanically, and use appropriately independent or human review for consequential judgment.

## Completion Language

Be boringly precise here:

- "Implemented and verified with `npm test`."
- "Content scaffold created; link check passes."
- "Could not run the production check because credentials were unavailable."

Avoid unsupported claims like "should work" when a relevant check was available but skipped.

## Failure Modes

- Running an unrelated broad test and treating it as proof.
- Skipping verification because the change looks simple.
- Claiming tests pass after a partial or failed run.
- Forgetting to mention unavailable checks.
- Changing the harness and its evaluator together without preserving a comparable baseline.
- Treating a generated eval as independent proof of the generator.

## Verification

A completion note is defensible when it states what changed, what was checked, what failed or was skipped, and what remains.
