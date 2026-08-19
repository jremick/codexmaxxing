# Thinking Abstraction Level

Abstraction level is one of the most useful controls in agentic work.

With older or weaker tooling, you had to drive close to the ground: exact prompts, exact steps, exact files, exact plan. That still works, but it leaves a lot of the value on the table.

With stronger frontier models, the better move is often to go up a level:

```mermaid
flowchart TD
  A["Tiny task"] --> B["Framed task"]
  B --> C["Outcome with success criteria"]
  C --> D["Broad goal with clear constraints"]
  D --> E["Codex derives the project harness"]
  E --> F["Codex executes and verifies"]
```

The human job shifts from "write every step" to "choose the right abstraction level."

## What Abstraction Level Means

Abstraction level describes how close a task statement is to the desired outcome versus an individual implementation action.

Low abstraction level:

```markdown
Change line 42 to use `color_temp_kelvin`.
```

Medium abstraction level:

```markdown
Fix the automation schema issue. Verify the target system accepts the configuration and the previous error stops appearing.
```

Higher abstraction level:

```markdown
The automations broke after an upgrade. Diagnose the likely failure layer, make the smallest safe fix, and verify the affected workflow is healthy again.
```

All three can be right. The useful judgment is knowing when Codex can take the higher-abstraction version and derive the work underneath it.

## Abstraction Is One Axis

Abstraction level describes the request, not the maturity of the system receiving it.

Three independent dimensions matter:

| Dimension | Question | Progression |
| --- | --- | --- |
| Intent abstraction | How much implementation is specified by the operator? | edit → task → outcome → system objective |
| System embodiment | Where does the operating method live? | prompt → reusable workflow → harness → orchestration system |
| Improvement closure | What changes future runs? | nothing → captured lesson → eval → governed promotion |

A broad prompt sent to a disposable agent is high in intent abstraction but low in system embodiment. A short request can initialize a mature system when its semantics, state, tools, checks, and authority boundaries already exist.

See [From Prompts To Compounding Systems](from-prompts-to-compounding-systems.md) for the complete model.

## The New Default

For bigger work, do not start by writing the task contract yourself.

Start with:

```markdown
Goal:
<what should be true>

Success criteria:
<what would prove it worked>

Constraints:
<scope, safety, style, time, privacy, compatibility>

Context:
<what matters, or where to look first>
```

Then ask Codex to derive only the artifacts the work needs, such as:

- the task contract,
- the source-of-truth map,
- the project harness,
- the agentic harness topology,
- the delivery harness,
- the verification plan,
- the stop conditions.

That is the difference between using Codex as a task executor and using it as an agentic operating system.

## When To Go Higher

Go higher when:

- the goal is clear but the path is not,
- the repo or system has enough context for Codex to inspect,
- success criteria can be stated,
- the work can be verified,
- the downside of a wrong plan is bounded by review or approval.

Stay lower when:

- the next action is risky,
- the target is fragile or destructive,
- the source of truth is not available,
- you already know the exact safe edit,
- ambiguity would cause expensive churn.

## The Abstraction Level Ladder

| Abstraction Level | You Provide | Codex Provides |
| --- | --- | --- |
| Exact edit | File, line, change | The edit and maybe a quick check |
| Framed task | Outcome, source, constraints | The steps and verification |
| Mission | Goal, success criteria, context | Task contract, plan, implementation, checks |
| System objective | Direction, policies, boundaries, invariants | Harness selection, orchestration, execution, evidence, change proposal |

A higher abstraction level does not mean less clarity. It means clarity moves from steps to outcomes, boundaries, and success criteria.

It also delegates more discretion. As abstraction rises, make scope, permissions, verification, and stop conditions more explicit. A broader goal never grants broader authority by itself.

## The Failure Mode

The bad version of this is vague delegation:

```markdown
Make this better.
```

That is not high abstraction. It is ambiguity.

High-abstraction work still has a shape:

```markdown
Make this repo feel like a public project someone would actually want to explore.

Success criteria:
- the README has a clear point of view,
- the first-click paths are obvious,
- internal maintenance notes are not part of the public surface,
- examples are synthetic and public-safe,
- validation still passes.
```

Codex can turn that into a task contract, plan, file edits, and checks.

## Why This Matters

The ceiling moves when the model can reason well enough to design the harness.

You stop spending all your energy decomposing work into tiny tickets and start spending more of it on:

- choosing better goals,
- defining better success criteria,
- giving better context,
- building better tools,
- keeping verification honest.

That is where Codex starts to feel less like autocomplete and more like a real operating layer for work.

The next ceiling is not a still-higher prompt. It is an environment in which a prompt initializes a versioned harness, verified evidence can improve future behavior, and authority remains explicit throughout the loop.
