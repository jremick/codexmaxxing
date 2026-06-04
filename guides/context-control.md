# Context Control

Context is not everything the agent can see.

Useful context is the stuff that can change the decision.

## Source Hierarchy

When sources conflict, choose deliberately. A good default order is:

1. What you just asked for.
2. Local project instructions.
3. Current repo files and tests.
4. Live read-backs when the task is about live state.
5. Official docs when current product behavior matters.
6. Prior memory and old notes.

Prior memory is useful for routing and preferences, but live state and current docs win when the fact can drift.

## Context Aperture

Open the aperture only as far as needed:

- For a bug fix, read the failing path, tests, callers, and local conventions.
- For a live incident, read health, logs, control-plane state, and relevant configs before changing anything.
- For current product claims, use official docs and record the verification date.
- For publication work, include privacy and source-safety checks.

## What To Say Explicitly

Tell Codex:

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
