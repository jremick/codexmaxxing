# Codex Operating Checklist

Use this before giving Codex a non-trivial mission.

## Abstraction Level

- The ask is at the right level: exact edit, task, outcome, or broad goal.
- Success criteria are clearer than the step list.
- Codex can derive the task contract when the path is not obvious.

## Frame

- Outcome is stated as something observable.
- Source of truth is named.
- Scope boundaries are explicit.
- Allowed writes are clear.
- Stop conditions are clear.

## Context

- Current user instruction is captured.
- Relevant repo files, docs, or live surfaces are identified.
- Volatile facts will be rechecked.
- Old memory is treated as routing context unless verified.
- Irrelevant adjacent work is out of scope.

## Tools

- Required capabilities are available, enabled, and discoverable on the selected host.
- Reads happen before writes.
- Secrets will not be printed or stored.
- External writes have approval or a clear allowed boundary.
- Codex has enough tool access to inspect before planning deeply.

## Environment

- Local, Worktree, or Cloud was chosen deliberately.
- Parallel writers have isolated filesystems or non-overlapping ownership.
- Local and remote runtime differences are explicit.
- Source, merged, deployed, and released states will not be conflated.

## Permissions

- The sandbox boundary is appropriate for the task.
- Approval points are separate from filesystem and network access.
- Browser, Computer Use, plugins, and MCP have their own reviewed boundaries.
- Higher abstraction or reasoning does not grant broader authority.

## Parallel Work

- The harness topology is named: single-thread, hub-and-spoke, pipeline, specialist team, or portfolio.
- Each agent or project stream has one owner and one source of truth.
- Write boundaries do not overlap unless the parent owns integration.
- Every stream has a status contract and proof path.

## Verification

- The primary check is named before completion.
- The check maps to the requested outcome.
- Skipped checks will be reported.
- The final answer will include what changed, what passed, and what remains.

## Output Surface

- The result belongs in chat, a repository file, an artifact, a visualization, or a Site.
- Visual files will be opened or rendered before completion.
- Deployment or publication has separate explicit authority.
- The chosen surface exists on the host where the work will run.

## Learning

- Repeated lessons have a destination: instructions, template, script, skill, docs, or backlog.
- One-off details are not promoted into durable rules.
