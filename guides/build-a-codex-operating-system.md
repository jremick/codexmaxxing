# Build A Codex Operating System

Codex gets stronger when the surrounding setup tells it what matters, gives it room to think at the right abstraction level, and preserves verified improvements across runs.

That setup does not need to be heavy. Most of the time it is just a few files, a few habits, and one or two checks that stop the agent from wandering off into the bushes.

## The Nine System Layers

### 1. Intent And Authority

Start by choosing the level of the ask. Are you asking for an exact edit, a framed task, an outcome, or a system objective?

Name who can request the work, what may be read or changed, and which transitions require approval. The higher the abstraction level, the more important explicit success criteria, permission boundaries, and stop conditions become.

### 2. Mission brief

Every non-trivial mission needs an outcome, source of truth, constraints, verification, and stop conditions. You can write these yourself, but often the better move is to ask Codex to draft them from the goal before execution.

### 3. Source And Semantic Model

Name the context that matters:

- repo files and tests,
- current user instruction,
- official docs,
- live APIs or deployed surfaces,
- issue trackers or planning docs,
- prior memory or decisions.

Also name what does not matter. Excluding stale or adjacent context is part of the job.

For workflows that cross multiple agents or systems, define the terms they must share: entities, states, relationships, provenance, and invariants. A small schema or vocabulary is often enough; do not introduce a large ontology without recurring semantic ambiguity.

### 4. Instructions And Routing

Use project instructions for repo-level defaults: coding style, useful commands, privacy boundaries, browser routes, and release gates. Keep them practical. If a rule applies to only one workflow, make it a checklist or skill instead. Keep routing explicit enough that Codex can find the narrow capability without loading the whole library.

### 5. Capability Surface

Give Codex the smallest capability surface needed for the work: project instructions, scripts, skills, plugins, MCP connectors, Browser, Computer Use, or ordinary shell and Git tools. Start read-only when the state is uncertain. Allow writes only when the source of truth and rollback boundary are clear. See [Skills, Plugins, MCP, And Tools](skills-plugins-mcp-and-tools.md).

### 6. Orchestration Graph

Name both who performs the work and how work moves. Is this one chat, a subagent workflow, separate worktree chats, a delivery pipeline, or a set of cloud tasks? Which dependencies, gates, state transitions, retries, and recovery paths connect them? See [Graph And Ontology-Engineered Harnesses](graph-and-ontology-engineered-harnesses.md) and [Local, Worktree, And Cloud Environments](environments-worktrees-and-cloud.md).

Do not automate a graph you cannot explain. Each node needs a source of truth, write boundary, status contract, evidence contract, and integration point.

### 7. State, Artifacts, And Evidence

Decide which state is task-local, durable, external, derived, or prohibited. Define required outputs and keep unresolved questions visible. Preserve provenance without collecting unnecessary sensitive content.

### 8. Verification And Observability

Define the check before claiming completion and capture enough structured evidence to diagnose failure. The right check is the one most likely to catch the wrong plausible result. A system-level check should also cover invariants, transitions, and recovery paths.

### 9. Governed Improvement

Repeated lessons can become reusable artifacts:

- instructions,
- templates,
- validators,
- scripts,
- skills,
- decision records,
- examples.

Promotion needs evidence. Turn recurring failures into regression checks, evaluate candidate changes against a preserved baseline, review permission changes separately, and keep a rollback path. Do not preserve private one-off detail as a global rule. See [Verified Improvement Loops](verified-improvement-loops.md).

## Minimal Setup For A Repo

Start with:

1. `README.md` that names the project and start paths.
2. project instructions with local conventions and checks.
3. one obvious verification command.
4. a mission brief template.
5. a fixture, demo, or tiny example if other people need to try it.

That is enough for many projects. Add CI, skills, MCP, and subagents when they remove real friction.

For a recurring workflow, add only the next useful layer: a versioned harness, a small state contract, one high-value eval, and a reviewed promotion path. A graph or ontology should earn its complexity.

## Failure Modes

- Treating Codex like a generic chatbot instead of an agentic operating system.
- Staying at a tiny-task abstraction level when the model could safely derive the harness.
- Spawning agents without an agentic harness topology.
- Adding broad instructions that never get used.
- Giving tool access without source-of-truth clarity.
- Verifying with a command unrelated to the change.
- Capturing every session note as permanent memory.
- Calling repeated automation "compounding" when no verified improvement changes future runs.
- Letting a system modify its active harness without a separate candidate, promotion gate, and rollback path.

## Verification

The operating system is working when a new task starts with less explanation, touches fewer unrelated files, and finishes with better proof. It is compounding when a verified lesson safely improves the next comparable run.
