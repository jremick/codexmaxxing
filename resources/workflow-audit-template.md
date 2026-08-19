# Workflow Audit Template

Use this to decide whether a recurring workflow is ready for Codexmaxxing.

```markdown
Workflow name:
Current owner:
Current trigger:
Current inputs:
Current output:
Abstraction level:
Current action mode: read-only / draft-only / action

Pain:
Frequency:
Risk:
Value if improved:

Source of truth:
Freshness requirements:
Data sensitivity:
Tools needed:
Allowed writes:
Human approval gates:

Current verification:
Better verification:

Smallest useful Codex pattern:
- assisted task
- verified task
- tool-connected workflow
- repeatable playbook
- operating redesign
- agentic operating system
- compounding system with a verified improvement loop

Reusable artifacts to create:

Do not automate:

Next experiment:
```

This works for more than software delivery. Example candidates include a weekly research digest, meeting follow-up, comparison shopping, travel planning, document production, inbox triage, content review, device checks, and repository maintenance.

## Decision Rules

- Start with high-frequency, low-risk workflows.
- Avoid automating unclear ownership.
- Add validation before adding broad tool access.
- Prefer playbooks before complex orchestration.
- Keep read-only, draft-only, and action permissions distinct.
- Do not turn private source material into reusable public context.
