# Mission Brief

Use this when the goal is bigger than a single task and you want Codex to design the plan underneath it.

```markdown
Goal:
Success criteria:
Constraints:
Context:

Ask Codex to work out:
- a short plan
- the sources that matter
- the checks
- the stop conditions
```

## Notes

- `Goal` should describe what is true when the work is done.
- `Success criteria` should describe what would make the result good.
- `Constraints` should name scope, safety, privacy, compatibility, style, or time boundaries.
- `Context` should point Codex at the first useful sources, not paste every possible thing.
- The plan is Codex's first output, not something you always need to write by hand.

## Example

This example is synthetic and uses no real person, organization, account, or environment details.

```markdown
Goal:
Turn these rough notes and source links into a short decision brief.

Success criteria:
- the decision is stated clearly,
- each option is compared against the same criteria,
- facts, inference, and unknowns are easy to distinguish,
- claims that may have changed are cited,
- the next human decision is obvious.

Constraints:
- keep it under two pages,
- do not invent missing facts,
- keep the source material private,
- stop at a draft; do not send or publish it.

Context:
Start with the supplied notes. Check only the external claims that could change the recommendation.

Ask Codex to work out the plan, relevant sources, checks, and stop conditions before editing.
```
