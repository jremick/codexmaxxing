# Context Control

Context is not everything the agent can see.

Useful context is the stuff that can change the decision.

Thinking altitude changes what context matters. At low altitude, Codex needs the exact file or command. At higher altitude, it needs the goal, constraints, examples of good work, tool access, and enough of the surrounding system to design a path.

## Source Hierarchy

When sources conflict, choose deliberately. A good default order is:

1. What you just asked for.
2. Success criteria and constraints.
3. Local project instructions.
4. Current repo files and tests.
5. Live read-backs when the task is about live state.
6. Official docs when current product behavior matters.
7. Prior memory and old notes.

Prior memory is useful for routing and preferences, but live state and current docs win when the fact can drift.

## Context Aperture

Open the aperture only as far as needed:

- For a bug fix, read the failing path, tests, callers, and local conventions.
- For a live incident, read health, logs, control-plane state, and relevant configs before changing anything.
- For current product claims, use official docs and record the verification date.
- For publication work, include privacy and source-safety checks.

## What To Say Explicitly

Tell Codex:

- "We are operating at outcome level; derive the task contract first."
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
