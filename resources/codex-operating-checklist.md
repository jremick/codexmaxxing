# Codex Operating Checklist

Use the quick check for ordinary work. The rest is for larger, repeated, parallel, or higher-risk work; it is not paperwork that every task must complete.

## Quick Check

- What should be true when the work is done?
- Where should Codex look first?
- What may it change, and what is out of scope?
- What check is most likely to catch a plausible mistake?
- Does any action need separate approval?

## Full Checklist For Bigger Or Repeated Work

### Abstraction Level

- The ask is at the right level: exact edit, task, outcome, or broad goal.
- Success criteria are clearer than the step list.
- Codex can work out the plan when the path is not obvious.
- A broader request is not being confused with a more mature system or broader permission.

### Frame

- Outcome is stated as something observable.
- Source of truth is named.
- Scope boundaries are explicit.
- Allowed writes are clear.
- Stop conditions are clear.

### Context

- Current user instruction is captured.
- Relevant repository files, documents, APIs, applications, or deployments are identified.
- Volatile facts will be rechecked.
- Old memory is treated as routing context unless verified.
- Irrelevant adjacent work is out of scope.

### Tools

- Required tools and capabilities are available, enabled, and discoverable on the selected host.
- Reads happen before writes.
- Secrets will not be printed or stored.
- External writes have approval or a clear allowed boundary.
- Codex has enough tool access to inspect before planning deeply.

### Environment

- Local, Worktree, or Cloud was chosen deliberately.
- Parallel writers have isolated filesystems or non-overlapping ownership.
- Local and remote runtime differences are explicit.
- Source, merged, deployed, and released states will not be conflated.

### Permissions

- The sandbox boundary is appropriate for the task.
- Approval points are separate from filesystem and network access.
- Browser, Computer Use, plugins, and MCP have their own reviewed boundaries.
- Higher abstraction or reasoning does not grant broader permission.

### Parallel Work, If Needed

- The team shape is named: single task, hub-and-spoke, pipeline, specialist team, or portfolio.
- Each agent or project stream has one owner and one source of truth.
- Write boundaries do not overlap unless the parent owns integration.
- Every stream has a clear update format and evidence path.

### Reusable System Design, If Needed

- The harness names its instructions, tools, routing, state, outputs, and checks.
- The agent team is distinguished from workflow order and dependencies.
- Shared entities, states, and relationships are defined only as deeply as recurring ambiguity requires.
- Failure, error, incomplete, and unknown states have explicit routes.
- Every write and state change has a permission and evidence boundary.

### Verification

- The primary check is named before completion.
- The check maps to the requested outcome.
- Skipped checks will be reported.
- The final answer will include what changed, what passed, and what remains.

### Output Format

- The result belongs in the task, a repository file, an artifact, a visualization, or a Site.
- Visual files will be opened or rendered before completion.
- Deployment or publication has separate explicit permission.
- The chosen format is supported on the host where the work will run.

### Learning

- Repeated lessons have a destination: instructions, template, script, skill, docs, or backlog.
- One-off details are not promoted into durable rules.
- Doing the work, checking it, and improving the workflow are separate.
- Candidate changes are versioned and evaluated against a preserved baseline.
- Permission and data-access changes receive separate review.
- Permission to adopt or roll back a change is explicit.
- Private evidence is generalized before becoming reusable guidance.
