# Field Patterns

These generalized patterns recur across research, planning, writing, operations, software, devices, documentation, and other everyday work.

The examples are synthetic and do not describe a specific person, repository, organization, or environment.

The central pattern is choosing the right abstraction level, then checking the real result. As models become more capable, a well-bounded goal can delegate more of the path while the operator retains responsibility for scope, permissions, and verification.

```mermaid
flowchart TD
  A["Choose abstraction level"] --> B["Goal + success criteria"]
  B --> C["Work out the plan"]
  C --> D["Design bounded approach"]
  D --> E["Execute"]
  E --> F["Human or system verifies"]
  F --> G{"Likely to repeat?"}
  G -->|no| H["Finish"]
  G -->|yes| I["Test a reusable improvement"]
```

The improvement branch is optional. A one-off task can finish after honest verification. Repeated work is where instructions, skills, scripts, evals, and other reusable pieces start to pay off.

## Live Systems: Read First, Then Touch Things

A reliable operations loop is deliberately conservative:

1. prove which layer is failing,
2. avoid unrelated changes,
3. make the smallest reversible move,
4. read the system back afterward.

```mermaid
flowchart LR
  A["Symptom"] --> B["Access?"]
  B --> C["Host/runtime?"]
  C --> D["Application integration?"]
  D --> E["Configuration/schema?"]
  E --> F["Data or presentation?"]
  F --> G["Small fix"]
  G --> H["Read-back"]
```

The pattern applies to deployed applications, local services, containers, devices, and other layered systems. Actual infrastructure details do not belong in a public example.

## Product Repositories: Provide A Safe Trial Path

A contributor-ready repository should have a way to run without private infrastructure.

That often means:

- fixture or demonstration data,
- a local run path,
- one clear verification command,
- secrets that remain outside the client and repository,
- and documentation that explains the happy path before the architecture tour.

When a workflow repeats, preserve the generalized method as a skill, checklist, template, or validator. Do not preserve the private source material that produced it.

## Parallel Work: Shape Before Swarm

Parallel work becomes useful when each stream has a clear job and handoff, not merely when more agents are running.

The durable pattern is:

- choose the work shape,
- split by ownership boundary,
- give every stream a simple update format,
- keep the parent responsible for integration,
- verify each result before treating it as progress.

The useful part is not the number of agents. It is the shape of the handoffs.

## Devices: The Real Target Gets A Vote

Device work is a useful antidote to agent overconfidence.

If software communicates with a phone, peripheral, display, or board, then "the code looks right" is not enough. Verification may need to reach the actual target:

```mermaid
sequenceDiagram
  participant Codex
  participant Repository
  participant Simulator
  participant Device

  Codex->>Repository: make the smallest change
  Repository->>Simulator: build and inspect
  Simulator-->>Codex: layout or test evidence
  Codex->>Device: install, flash, or launch
  Device-->>Codex: observed runtime evidence
```

The final report should distinguish source inspection, build evidence, simulation, and physical-device behavior.

## Everyday Work Uses The Same Loop

Useful agent work also includes:

- researching a decision from current sources,
- comparing products, services, routes, or approaches,
- planning around timing, location, budget, access, and preferences,
- turning notes, transcripts, images, and links into a useful result,
- drafting communication for a real audience,
- producing a document, spreadsheet, presentation, diagram, or interactive explanation,
- reviewing records, reminders, or updates on a recurring schedule.

The check changes with the work:

| Work | Useful check |
| --- | --- |
| research or comparison | sources are current, criteria are consistent, uncertainty is visible |
| planning | changing constraints were checked and no booking or purchase is implied |
| notes or transcript synthesis | names, dates, claims, and actions match the source material |
| communication | the draft says the real thing, fits the audience, and makes no unsupported promise |
| artifact production | the content is correct and the rendered result is usable |
| recurring review | the source is current, the signal is useful, and the action boundary was respected |

Name the outcome, load only the necessary context, do the work, and check the result. Keep external actions such as sending, publishing, booking, buying, or deleting behind explicit approval.

## The Pattern Underneath

Strong Codex workflows usually combine:

- an appropriate abstraction level,
- a clear task shape,
- narrow authoritative context,
- bounded tool access,
- claim-specific checks,
- reusable generalized learning.

When those pieces are missing, fluent output can be mistaken for verified progress.
