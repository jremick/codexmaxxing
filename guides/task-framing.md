# Task Framing For Agents

Good agent work starts with work that can be proven done.

The goal is not to write a perfect prompt. It is to choose the right abstraction level.

Sometimes that means a tight task. Sometimes it means a broad goal with sharp success criteria, then asking Codex to work out the plan itself.

## A Useful Frame

This is still useful for bounded tasks:

```markdown
Goal: <what should be true at the end>
Source of truth: <repo, doc, live system, issue, or user instruction>
Constraints: <scope limits, privacy rules, compatibility requirements>
Verification: <commands, checks, screenshots, read-backs, review gates>
Stop conditions: <what should pause the work>
```

## For Bigger Work

For bigger work, use a goal-shaped frame:

```markdown
Goal: <what should be true>
Success criteria: <what would make this good>
Constraints: <scope, safety, style, compatibility, privacy>
Context: <where to look first, or what matters most>

First work out the plan, the sources that matter, and the verification path. Then execute.
```

That small difference matters. The operator is not doing all the decomposition for Codex. The goal supplies enough context and discretion for Codex to propose the path.

## When A Reusable Workflow Already Exists

When a mature reusable workflow already exists, the prompt can be smaller because it starts known layers instead of restating them:

```markdown
Objective: <what should be true>
Workflow or harness: <versioned workflow to use>
Inputs: <current sources or event>
Permissions: <allowed reads, writes, and approval gates>
Evidence required: <checks or artifacts for this run>

Use the current approved version. Propose any reusable improvement separately from this run.
```

This only works when the referenced workflow is real, discoverable, and versioned. Naming an imaginary system is not a substitute for building one.

## What To Include

Name the real target. If the task is about production, say production. If it is about a local branch, say that. If a document is authoritative, name it.

Name the boundary. A good boundary prevents helpful-looking drift: no adjacent refactors, no new framework, no public release, no live write, or no auth changes.

Name the proof. Evidence must match the claim: tests and validators can check deterministic behavior, API read-backs can confirm service state, and browser inspection or screenshots can support rendered-state claims. None proves a different layer by itself. When the work is subjective, state the quality bar clearly enough for deliberate review.

## What To Avoid

Try not to give Codex tasks that only describe effort:

- "Investigate this."
- "Clean it up."
- "Make it better."
- "Think deeply."

Those can be useful starts, but they need either success criteria or a request for Codex to derive them before they become executable.

## Verification

The frame is good enough when Codex can derive a sensible plan, execute without broad guessing, and point to concrete evidence at the end.
