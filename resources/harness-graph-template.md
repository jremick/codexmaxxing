# Workflow Graph Template

Use this advanced template when a workflow has meaningful dependencies, branching, state changes, or recovery paths. If the work is linear, use a checklist instead.

## Workflow

```markdown
Graph name:
Objective:
Version:
Entry condition:
Completion condition:
Rules that must always hold:
Prohibited state or data:
Who can approve a new version:
Rollback target:
```

## Step

Repeat for each node:

```yaml
id: <stable_node_id>
purpose: <one observable responsibility>
owner: <agent, person, service, or deterministic process>
reads: []
writes: []
permissions: <read_only | bounded_write | approval_required>
preconditions: []
success_conditions: []
evidence: []
timeout_or_budget: <bound>
failure_route: <node_id_or_stop>
```

## Connection

Repeat for each edge:

```yaml
from: <node_id>
to: <node_id>
condition: <observable transition condition>
passes: []
on_failure: <node_id_or_stop>
```

## Review Questions

- Does every write have one accountable owner?
- Does every transition rely on observable evidence?
- Can failures, errors, incomplete results, and unknowns remain visible?
- Are permissions and data exposure narrower than the union of all steps?
- Can the graph resume safely after interruption?
- Can a proposed graph be evaluated without replacing the current graph?
- Is a graph actually needed, or would a linear checklist be clearer?

The YAML fragments are an illustrative format, not built-in Codex syntax.
