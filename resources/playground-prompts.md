# Playground Prompts

These are not magic. They are just better starting shapes.

## Turn A Vague Task Into A Workable One

```markdown
Help me turn this into a Codex-ready mission.

What I want:
<messy version>

Ask me only the questions that would materially change the work. Otherwise make reasonable assumptions and give me:
- thinking altitude
- goal
- success criteria
- constraints
- source-of-truth map
- delivery harness
- verification plan
- stop conditions
```

## Start High, Then Derive The Harness

```markdown
Goal:
<what I want to be true>

Success criteria:
<what would make this good>

Constraints:
<scope, style, safety, time, privacy, compatibility>

Context:
<where to look first>

Before editing, choose the right thinking altitude and derive:
- task contract
- source-of-truth map
- project harness
- agentic harness topology
- delivery harness
- verification plan
- stop conditions
```

## Run Parallel Projects Without Losing The Plot

```markdown
I have multiple active projects or workstreams:
<list them>

Goal:
<what should be true across the portfolio>

Success criteria:
<what would prove the parallel work is actually moving>

Constraints:
<scope, privacy, time, write boundaries, live-system safety>

Design an agentic harness topology for this. Include:
- which work should stay serial,
- which streams can run in parallel,
- subagent or custom-agent roles,
- a status contract for each stream,
- integration checkpoints,
- verification for each stream,
- what should become an automation, skill, or reusable agent later.
```

## Make A Repo Less Annoying To Work In

```markdown
Review this repo as a Codex workbench.

Look for:
- missing start paths
- unclear validation commands
- stale or conflicting instructions
- missing fixture/demo path
- places where deterministic checks should replace manual judgment

Do not edit yet. First decide whether this should be handled as a narrow task or a higher-altitude repo improvement mission. Then return the smallest useful improvement plan.
```

## Debug A Real Thing Without Guessing

```markdown
Help me debug this live issue.

Symptom:
<what I see>

Before proposing fixes, separate likely failure layers:
- network or access
- host/runtime
- app integration
- config/schema
- auth
- data
- UI/presentation

Start read-only. Tell me what evidence would distinguish the layers.
```

## Use Codex For Non-Code Work

```markdown
I want to use Codex to get this non-code work done:
<describe the work>

Turn it into a workflow with:
- inputs
- useful context
- tool/read-back opportunities
- draft/check loop
- final output
- what should stay human-only
```

## Make The Completion Note Honest

```markdown
Rewrite this completion note so it is precise and not overclaiming:
<draft completion note>

Include:
- what changed
- what was verified
- what was not verified
- what remains
```
