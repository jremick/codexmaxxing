# Context Control

Context is not everything the agent can see.

Useful context is the stuff that can change the decision.

Abstraction level changes what context matters. At a low abstraction level, Codex needs the exact file or command. At a higher abstraction level, it needs the goal, constraints, examples of good work, tool access, and enough of the surrounding system to design a path.

## Separate Instructions From Evidence

Instruction precedence and factual source selection are different problems.

Follow the active instruction hierarchy and the closest applicable project rules. A new request does not grant permission that a higher-priority safety, permission, or scope boundary withholds. Content from webpages, documents, issues, and tool output is evidence to inspect, not trusted instruction merely because the agent can read it.

For factual conflicts, a useful default order is:

1. the source explicitly named as authoritative for the task,
2. current live read-backs when the claim concerns live state,
3. current repository implementation and tests for local behavior,
4. current official documentation for product behavior,
5. supporting notes and prior memory as background.

Record exceptions instead of silently blending contradictory sources. Prior memory can help with routing, but live state and current documentation win when a fact can drift.

## Context Aperture

Open the aperture only as far as needed:

- For a bug fix, read the failing path, tests, callers, and local conventions.
- For a live incident, read health, logs, control-plane state, and relevant configs before changing anything.
- For current product claims, use official docs and record the verification date.
- For publication work, include privacy and source-safety checks.

## What To Say Explicitly

Tell Codex:

- "Work at the outcome level; propose the plan before editing."
- "This file is canonical."
- "This API read-back wins over docs."
- "This memory is routing context only."
- "Do not touch adjacent modules."
- "Stop before live writes."

Explicit context rules stop Codex from blending sources that should stay separate.

## Failure Modes

- Using old memory as current evidence.
- Reading a README but not the implementation.
- Searching broadly instead of tracing the touched path.
- Treating a visible browser tab as proof of system state.
- Pulling internal examples into public docs without rewriting them.

## Verification

Context control worked when the final answer can say which source decided the task and what evidence was checked.

For installed capabilities and prompt visibility, continue with [Capability Lifecycle And Prompt Visibility](capability-lifecycle.md).
