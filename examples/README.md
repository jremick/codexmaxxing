# Example Missions

Codexmaxxing makes more sense when it is attached to a well-defined mission.

All examples are synthetic. Their names, paths, systems, and evidence are placeholders and do not describe a specific person, repository, organization, or environment.

The point is not to pre-chew every task. Give Codex an appropriate abstraction level, success criteria, and the right context. Let it design the plan underneath.

## 0. Broad Goal: Let Codex Build The Harness

```markdown
Goal:
Turn this rough repo into a public-facing project that people can understand, explore, and reuse.

Success criteria:
- the README has a clear point of view,
- the first-click paths are obvious,
- examples include technical and non-technical work,
- examples are synthetic and public-safe,
- internal maintenance notes are not part of the public surface,
- validation still passes.

Constraints:
- keep the voice casual, practical, and technical,
- avoid work-presentation energy,
- keep private details out.

Context:
Start with README, docs, guides, resources, and examples.

Before editing, choose the appropriate abstraction level and derive only the task contract, delivery steps, verification plan, and stop conditions that the work needs.
```

Good for: repo shaping, product positioning, docs overhaul, public launch prep.

## 1. Product Repo: Make It Runnable

```markdown
Goal:
Make this repository runnable by a new contributor without access to private infrastructure.

Review the README, env examples, scripts, tests, and demo/fixture path.
Find the smallest set of changes that would make the repo contributor-friendly.
Do not assume access to private services.
Verify with the repo's normal checks.
```

Good for: app repos, CLI tools, open-source cleanup, public project polish.

## 2. Live Issue: Stop Guessing

```markdown
Something is broken:
<symptom>

Start read-only. Separate possible causes by layer:
- network/access
- host/runtime
- app integration
- config/schema
- auth
- data
- UI/presentation

Tell me what evidence would distinguish them, then gather the safe evidence first.
```

Good for: local services, deployed applications, integrations, and intermittent failures.

## 3. Hardware Loop: The Device Decides

```markdown
Make this hardware/UI change, but do not stop at code.

Expected result:
<observable behavior>

Verification path:
1. build
2. run focused tests if available
3. inspect simulator or mock UI if relevant
4. flash/install/launch on the real target
5. report exactly what was proven
```

Good for: mobile applications, firmware, peripherals, devices, dashboards, and any workflow where the real target matters.

## 4. Non-Code Work: Make The Mess Useful

```markdown
Source notes and rough goal:
<paste notes>

Turn this into:
- the real point
- the decision or output needed
- missing context
- a suggested structure
- a draft/check loop
- what should stay human judgment
```

Good for: writing, research, trip planning, comparison shopping, strategy notes, meeting follow-up.

## 5. Parallel Portfolio: Keep Multiple Threads Moving

```markdown
Active workstreams:
- <project 1>
- <project 2>
- <project 3>

Goal:
Keep useful progress moving without mixing context, losing blockers, or over-delegating.

Success criteria:
- each project has a current state,
- the next useful action is visible,
- parallelizable work is separated from serial work,
- every delegated stream has a proof path,
- the parent thread has clear integration checkpoints.

Design the agentic harness topology first. Then recommend which work should stay with the parent, which should go to subagents or custom agents, and what status contract each stream should use.
```

Good for: small portfolios, multi-repository cleanup, launch preparation, and research paired with implementation.

## 6. Choose The Execution Surface

```markdown
Goal:
Complete these independent workstreams without overlapping writes:
- <read-heavy investigation>
- <bounded repository change>
- <recurring follow-up>

Before executing, decide which work belongs in:
- the parent chat,
- subagents,
- a separate worktree chat,
- a cloud task,
- a scheduled task.

Explain the ownership, permission, integration, and verification boundary for each choice. Do not create parallel writers against the same files.
```

Good for: work that appears parallel but needs different execution environments.

## 7. Choose The Capability Layer

```markdown
Recurring workflow:
<synthetic workflow description>

Decide whether the smallest durable solution is:
- project instructions,
- a checklist or template,
- a deterministic script,
- a skill,
- a plugin,
- an MCP connector,
- a scheduled task.

Prefer the smallest layer that changes behavior reliably. Keep credentials, actual environment inventories, and private examples out of the artifact.
```

Good for: turning repeated work into a maintainable operating layer.

## 8. Choose The Output Surface

```markdown
Source material:
<synthetic inputs>

Desired use:
<how the result will be reviewed or explored>

Choose between:
- a document, spreadsheet, presentation, or PDF,
- a static chart or diagram,
- an interactive visualization,
- a hosted Site,
- repository-native code.

State the visual checks, deterministic checks, privacy boundary, and whether deployment is authorized. Do not deploy merely because creation is authorized.
```

Good for: artifact production, interactive explanations, dashboards, and hosted experiences.

## 9. Engineer A Compounding Workflow

```markdown
Recurring workflow:
<synthetic workflow description>

Observed recurring failure:
<what repeatedly goes wrong and what evidence supports it>

Goal:
Turn the workflow into the smallest reliable, versioned harness that can improve through reviewed evidence.

Before implementing:
1. define the harness contract: instructions, tools, routing, state, outputs, and validation,
2. model only the dependencies and shared terms that affect correctness,
3. separate the execution, verification, and evolution loops,
4. define one regression case for the recurring failure,
5. define candidate, promotion, and rollback states,
6. identify privacy, privilege-expansion, feedback-poisoning, and self-confirmation risks.

Keep examples synthetic. Do not expose actual environment inventories, traces, credentials, private documents, or security controls.
```

Good for: recurring delivery, review, documentation, operations, research, and maintenance workflows that already have observable inputs and outcomes.

## The Common Shape

```mermaid
flowchart LR
  A["Intent"] --> B["Versioned harness"]
  B --> C["Execution"]
  C --> D["Evidence"]
  D --> E["Verification"]
  E --> F["Reviewed improvement"]
  F --> B
```

The domain changes. The loop mostly does not.
