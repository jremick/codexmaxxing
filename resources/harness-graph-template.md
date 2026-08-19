# Harness Graph Template

Use this template when a workflow has meaningful dependencies, branching, state transitions, or recovery paths.

## Graph Contract

```markdown
Graph name:
Objective:
Version:
Entry condition:
Completion condition:
Global invariants:
Prohibited state or data:
Promotion authority:
Rollback target:
```

## Node Contract

Repeat for each node:

```yaml
id: <stable_node_id>
purpose: <one observable responsibility>
owner: <agent, person, service, or deterministic process>
reads: []
writes: []
authority: <read_only | bounded_write | approval_required>
preconditions: []
success_conditions: []
evidence: []
timeout_or_budget: <bound>
failure_route: <node_id_or_stop>
```

## Edge Contract

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
- Are authority and data exposure narrower than the union of all nodes?
- Can the graph resume safely after interruption?
- Can a candidate graph be evaluated without replacing the promoted graph?
- Is a graph actually needed, or would a linear checklist be clearer?

The YAML fragments are illustrative contracts, not built-in Codex syntax.
