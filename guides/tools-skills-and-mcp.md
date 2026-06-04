# Tools, Skills, And MCP

Codex has a bunch of ways to get more capable. The trap is adding every shiny thing at once.

Use the smallest thing that changes behavior reliably.

At higher thinking altitude, tools and skills matter more. You are no longer asking Codex to do one edit. You are asking it to design and run a mini operating system around the goal.

## The Ladder

### Instructions

Use project instructions for local rules that should always apply in a repo: test commands, privacy boundaries, coding conventions, browser routes, release gates.

### Mission briefs

Use a mission brief when you know the goal and success criteria but want Codex to derive the task contract, plan, and checks.

### Templates and checklists

Use Markdown resources when the workflow needs human judgment but not automation. A good template is often better than a premature tool.

### Scripts and validators

Use code when the check is deterministic: link validation, schema checks, formatting, package parity, release gates.

### Skills

Use a skill when a repeatable workflow needs instructions, examples, helper scripts, and routing rules. Skills are useful when "how to do the work" is itself reusable.

### MCP tools

Use MCP or connectors when Codex needs structured access to external systems: GitHub, docs, databases, issue trackers, browsers, internal knowledge, or APIs.

### Automations

Use automations for recurring checks, reminders, monitors, or scheduled reviews. Keep them read-only or draft-only unless the action boundary is very clear.

## Selection Rule

Ask:

- Is this judgment? Use a guide or checklist.
- Is this exact and repeatable? Use a script or validator.
- Is this a recurring workflow? Use a skill.
- Does Codex need a real system? Use MCP or a connector.
- Does it need to happen on a schedule? Use an automation.
- Is the goal clear but the path unclear? Use a mission brief and let Codex derive the harness.

## Tool Safety

Tool access should come with boundaries:

- default to read-only exploration,
- avoid printing secrets,
- use least privilege,
- require approval for external writes,
- verify with read-back after writes.

## Verification

The capability choice is right when it reduces repeated explanation, improves proof, and does not add more operational weight than the task deserves.
