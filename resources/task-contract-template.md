# Mission Brief Template

Use this when the goal is bigger than a single task and you want Codex to design the plan underneath it.

```markdown
Goal:
Success criteria:
Constraints:
Context:

Ask Codex to derive:
- task contract
- source-of-truth map
- delivery harness
- verification plan
- stop conditions
```

## Notes

- `Goal` should describe what is true when the work is done.
- `Success criteria` should describe what would make the result good.
- `Constraints` should name scope, safety, privacy, compatibility, style, or time boundaries.
- `Context` should point Codex at the first useful sources, not paste every possible thing.
- The derived contract is Codex's first output, not something you always need to write by hand.

## Example

```markdown
Goal:
Make this repo feel like a public project someone would actually want to explore.

Success criteria:
- the README has a clear point of view,
- first-click paths are obvious,
- related repos are linked,
- examples show code and non-code use,
- validation still passes.

Constraints:
- keep it casual and technical,
- remove internal maintenance framing,
- do not publish private examples.

Context:
Start with README, guides, resources, examples, and related-project docs.

Ask Codex to derive the task contract, source-of-truth map, delivery harness, verification plan, and stop conditions before editing.
```
