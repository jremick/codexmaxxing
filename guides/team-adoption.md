# Team Adoption

Codex adoption is not a tool rollout. It is work redesign.

Teams get value when they turn recurring work into clearer inputs, better tool access, reviewable outputs, and feedback loops that actually show whether anything improved.

## Start With Workflows

Pick a workflow that already happens:

- bug triage,
- dependency updates,
- release notes,
- support diagnostics,
- documentation maintenance,
- test expansion,
- incident review,
- internal tool cleanup.

Then wrap the Codex loop around that workflow.

## Capability Questions

Ask:

- Can people frame the task as an outcome with proof?
- Does Codex have access to the right source of truth?
- Are writes gated at the right points?
- Is there a deterministic check?
- Who reviews the output?
- Where does reusable learning go?
- How will the team know whether this saved time or improved quality?

## Adoption Levels

### 1. Assisted tasks

People use Codex for narrow drafting, search, small code changes, and explanations.

### 2. Verified tasks

Codex runs tests, checks links, validates configs, and reports evidence.

### 3. Tool-connected workflows

Codex uses GitHub, docs, browsers, databases, or internal systems through controlled connectors.

### 4. Repeatable playbooks

The team maintains `AGENTS.md`, templates, validators, and examples for recurring workflows.

### 5. Operating redesign

The team changes how work enters, flows, gets reviewed, and gets measured because Codex can now execute parts of it.

## What To Measure

- time to first useful draft,
- time to verified completion,
- defect rate after agent-assisted changes,
- review findings caught before merge,
- repeated questions eliminated by instructions or templates,
- workflows converted into playbooks,
- tasks that still require human-only judgment.

## Failure Modes

- Counting usage instead of outcomes.
- Treating agents as a replacement for source-of-truth clarity.
- Giving broad tool access without review gates.
- Publishing internal examples without rewriting them.
- Training people on prompts but not on verification.

## Verification

A team adoption effort is working when different people can run the same kind of workflow with similar inputs, similar checks, and a completion standard that does not depend on trusting the most confident person in the room.
