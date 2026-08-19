# Build A Codex Operating System

Codex gets stronger when the surrounding setup tells it what matters, gives it room to think at the right abstraction level, and keeps the useful parts of earlier work.

That setup does not need to be heavy. Most of the time it is just a few files, a few habits, and one or two checks that stop the agent from wandering off into the bushes.

## Start Light

Most projects need five things.

### 1. Outcome And Boundaries

Start by choosing the level of the ask. Are you asking for an exact edit, a framed task, an outcome, or a system objective?

Name what should be true, what Codex may read or change, what is out of scope, and which actions need approval. The higher the abstraction level, the more important clear success criteria and stop conditions become.

### 2. Sources And Context

Point Codex at the sources that can change the decision: repository files and tests, the current instruction, official documentation, a live API or deployment, or a relevant issue or decision record.

Also say what does not matter. Excluding stale or adjacent context is part of the job.

### 3. Instructions And Tools

Use project instructions for durable local rules: useful commands, coding style, privacy boundaries, and release gates. If a rule applies to one workflow, keep it in that workflow instead of making it global.

Give Codex the smallest set of tools it needs. Start read-only when the state is uncertain. Allow writes only when the source of truth, approval boundary, and rollback path are clear. See [Skills, Plugins, MCP, And Tools](skills-plugins-mcp-and-tools.md).

### 4. Shape Of The Work

Keep the work in one task when judgment is tightly connected or edits overlap. Split it when the workstreams are genuinely independent and each has a clear owner, output, and integration point.

If order, branching, retries, or recovery affect correctness, draw the workflow. Otherwise a short plan is enough. See [Workflow Graphs, Shared Vocabulary, And Harnesses](graph-and-ontology-engineered-harnesses.md) and [Local, Worktree, And Cloud Environments](environments-worktrees-and-cloud.md).

### 5. Checks

Define the check before claiming completion. The right check is the one most likely to catch a plausible but wrong result. Use tests for deterministic behavior, rendered or browser inspection for visible behavior, and live read-backs for live state.

## Add Only What Repeats

When a workflow keeps coming back, move the stable parts out of the prompt:

- repeated instructions can become project guidance or a skill;
- exact transforms and checks can become scripts or validators;
- useful output shapes can become templates;
- recurring failures can become regression cases;
- recurring handoffs can become a small workflow graph.

If several agents or systems keep disagreeing about terms, define a small shared vocabulary or schema. If the distinction is not causing failures, ordinary prose is enough.

Keep only the evidence needed to understand the result and diagnose failure. Do not collect raw prompts, private documents, credentials, or unrestricted traces merely because they might be useful later.

Improvements should be proposed separately from the run that discovered them. Compare the current and proposed versions, review permission changes separately, and keep a rollback path. See [Verified Improvement Loops](verified-improvement-loops.md).

## Minimal Setup For A Repo

Start with:

1. `README.md` that names the project and start paths.
2. project instructions with local conventions and checks.
3. one obvious verification command.
4. a short mission brief for bigger work.
5. a fixture, demo, or tiny example if other people need to try it.

That is enough for many projects. Add CI, skills, MCP, and subagents when they remove real friction.

For recurring work, add only the next useful piece: a reusable workflow, one high-value check, and a reviewed way to adopt or reject changes. A graph or ontology should earn its complexity.

## Failure Modes

- Treating Codex like a generic chatbot instead of giving it a clear outcome and useful environment.
- Staying at a tiny-task abstraction level when the model could safely derive more of the path.
- Splitting work across agents without clear ownership and integration.
- Adding broad instructions that never get used.
- Giving tool access without a clear source of truth and permission boundary.
- Verifying with a command unrelated to the change.
- Capturing every session note as permanent memory.
- Calling repeated automation "compounding" when no verified improvement changes future runs.
- Letting a system modify its active workflow without a separate candidate, approval gate, and rollback path.

## Verification

The operating system is working when a new task starts with less explanation, touches fewer unrelated files, and finishes with better evidence. It is compounding when a verified lesson safely improves the next comparable run.
