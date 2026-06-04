# Task Framing For Agents

Good agent work starts with a task that can be proven done.

The goal is not to write a perfect prompt. The goal is to give Codex enough shape to choose useful actions and stop at the right time.

## The Frame

For non-trivial work, I usually want this shape:

```markdown
Goal: <what should be true at the end>
Source of truth: <repo, doc, live system, issue, or user instruction>
Constraints: <scope limits, privacy rules, compatibility requirements>
Verification: <commands, checks, screenshots, read-backs, review gates>
Stop conditions: <what should pause the work>
```

## What To Include

Name the real surface. If the task is about production, say production. If it is about a local branch, say that. If a doc is canonical, name it.

Name the boundary. A good boundary prevents helpful-looking drift: no adjacent refactors, no new framework, no public release, no live write, or no auth changes.

Name the proof. The strongest proof is deterministic: a test, diff, validator, API read-back, screenshot, or command output. When the work is subjective, use a review checklist and state the criteria.

## What To Avoid

Try not to give Codex tasks that only describe effort:

- "Investigate this."
- "Clean it up."
- "Make it better."
- "Think deeply."

Those can be useful starts, but they need a proof point before they become executable.

## Verification

The frame is good enough when Codex can start without asking broad questions and the final answer can point to concrete evidence.
