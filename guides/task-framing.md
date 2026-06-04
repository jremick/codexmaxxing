# Task Framing For Agents

Good agent work starts with work that can be proven done.

The goal is not to write a perfect prompt. It is to choose the right altitude.

Sometimes that means a tight task. Sometimes it means a broad goal with sharp success criteria, then asking Codex to write the task contract and delivery plan itself.

## The Old Useful Frame

This is still useful for bounded tasks:

```markdown
Goal: <what should be true at the end>
Source of truth: <repo, doc, live system, issue, or user instruction>
Constraints: <scope limits, privacy rules, compatibility requirements>
Verification: <commands, checks, screenshots, read-backs, review gates>
Stop conditions: <what should pause the work>
```

## The Higher-Altitude Frame

For bigger work, I prefer this:

```markdown
Goal: <what should be true>
Success criteria: <what would make this good>
Constraints: <scope, safety, style, compatibility, privacy>
Context: <where to look first, or what matters most>

First derive the task contract, source-of-truth map, delivery harness, and verification plan. Then execute.
```

That tiny difference matters. You are not doing all the decomposition for Codex. You are giving it enough altitude and enough runway to design the decomposition.

## What To Include

Name the real surface. If the task is about production, say production. If it is about a local branch, say that. If a doc is canonical, name it.

Name the boundary. A good boundary prevents helpful-looking drift: no adjacent refactors, no new framework, no public release, no live write, or no auth changes.

Name the proof. The strongest proof is deterministic: a test, diff, validator, API read-back, screenshot, or command output. When the work is subjective, state the taste or quality bar clearly enough that Codex can review against it.

## What To Avoid

Try not to give Codex tasks that only describe effort:

- "Investigate this."
- "Clean it up."
- "Make it better."
- "Think deeply."

Those can be useful starts, but they need either success criteria or a request for Codex to derive them before they become executable.

## Verification

The frame is good enough when Codex can derive a sensible plan, execute without broad guessing, and point to concrete evidence at the end.
