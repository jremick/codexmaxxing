---
title: Verification Before Completion
status: draft
audience: Codex users who want defensible completion claims
updated: 2026-06-04
---

# Verification Before Completion

The final answer should not be the first time a task becomes precise. Verification turns completion from a claim into evidence.

## Principle

Choose the check that would catch the most likely wrong-but-plausible result.

For a code change, that might be a focused test or build. For a UI change, it might be a browser screenshot across viewports. For documentation, it might be a link check and a private-detail scan.

## Verification Ladder

Use the smallest rung that proves the task:

1. Static check: formatting, linting, schema validation, link checking.
2. Unit or focused behavior check.
3. Integration check across the touched boundary.
4. Live read-back or browser inspection.
5. Human review for subjective quality.

Higher is not always better. A live check can be overkill for a typo fix. A static check is too weak for a behavioral change.

## Completion Language

Be precise:

- "Implemented and verified with `npm test`."
- "Content scaffold created; local validator passes."
- "Could not run the production check because credentials were unavailable."

Avoid unsupported claims like "should work" when a relevant check was available but skipped.

## Failure Modes

- Running an unrelated broad test and treating it as proof.
- Skipping verification because the change looks simple.
- Claiming tests pass after a partial or failed run.
- Forgetting to mention unavailable checks.

## Verification

A completion note is defensible when it states what was changed, what was checked, what failed or was skipped, and what remains.
