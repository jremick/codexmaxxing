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

This example is synthetic and uses no real repository or environment details.

```markdown
Goal:
Make this repo feel like a public project someone would actually want to explore.

Success criteria:
- the README has a clear point of view,
- first-click paths are obvious,
- examples are synthetic and public-safe,
- examples show code and non-code use,
- validation still passes.

Constraints:
- keep it casual and technical,
- remove internal maintenance framing,
- do not publish private examples.

Context:
Start with README, guides, resources, and examples.

Ask Codex to work out the plan, relevant sources, checks, and stop conditions before editing.
```
