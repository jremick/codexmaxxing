# Example Missions

Codexmaxxing makes more sense when it is attached to a well-defined mission.

All examples are synthetic. Their names, paths, systems, and evidence are placeholders and do not describe a specific person, repository, organization, or environment.

The point is not to pre-chew every task. Say what you want, make the important limits clear, and let Codex design the plan underneath. Use the amount of structure the work needs; these do not have to become forms.

## 0. Broad Goal: Let Codex Work Out The Path

```markdown
Turn this rough repo into a public-facing project that people can understand, explore, and reuse.

Start with the README, docs, guides, resources, and examples. Work out the plan before editing.

The finished repo should have a clear point of view, obvious first-click paths, useful technical and non-technical examples, and passing validation. Keep the voice casual, practical, and technical. Remove internal maintenance framing and keep every example synthetic and public-safe.
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

Recommend what should stay in the main task, what can safely go to subagents or separate tasks, and how each stream should report progress and evidence. Keep the setup as simple as the work allows.
```

Good for: small portfolios, multi-repository cleanup, launch preparation, and research paired with implementation.

## 6. Choose Where The Work Should Run

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

## 8. Choose The Output Format

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

Help me turn this into the smallest reusable workflow that will make later runs more reliable.

Start simple. Tell me what should stay in the prompt, what belongs in instructions, a skill, a script, or a check, and where human approval still matters. Add a workflow graph or shared schema only if order, branching, recovery, or inconsistent language is causing real problems.

Turn the recurring failure into a regression case. Test any proposed workflow change against the current version before adopting it, keep a rollback path, and check for privacy, broader permissions, bad feedback, and self-confirming tests.

Keep examples synthetic. Do not expose actual environment inventories, traces, credentials, private documents, or security controls.
```

Good for: recurring delivery, review, documentation, operations, research, and maintenance workflows that already have observable inputs and outcomes.

## The Common Shape

```mermaid
flowchart LR
  A["Outcome"] --> B["Work"]
  B --> C["Check"]
  C --> D{"Likely to repeat?"}
  D -->|no| E["Finish"]
  D -->|yes| F["Make the useful part reusable"]
  F --> G["Test the next version"]
  G --> B
```

The domain changes. The loop mostly does not.
