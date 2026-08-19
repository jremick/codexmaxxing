# Compounding System Canvas

Use this for a recurring workflow that may deserve a reusable harness or coordinated system. Most workflows need only the quick version. Use the full canvas when risk, branching, shared state, or several agents and systems make the extra detail useful.

## Quick Version

```markdown
What keeps repeating?
What usually goes wrong?
What should be reusable next time?
What evidence would show an improvement?
What must stay under human approval?
What is the smallest useful change to try?
```

## Full Canvas

```markdown
System objective:
What one successful run produces:
System boundary:
Explicit non-goals:

Intent and permissions:
- Who can request a run?
- What may the system read?
- What may it write?
- Which transitions require approval?

Shared vocabulary or schema:
- Important things:
- Important relationships:
- Allowed states:
- Rules that must always hold:
- Meaning of failure, error, incomplete, and unknown:

Harness:
- Instructions and policies:
- Tools and capabilities:
- Routing rules:
- Required outputs:
- Validation checks:

Workflow graph, only if needed:
- Nodes:
- Dependency and control-flow edges:
- State passed between nodes:
- Failure and recovery routes:
- Integration point:

Evidence:
- Required events or records:
- Where artifacts and claims came from:
- Deterministic checks:
- Independent or human checks:
- Data that must not be collected:

Improvement loop:
- Feedback sources:
- Regression suite:
- Proposed-change process:
- Adoption gate:
- Rollback path:
- Possible regressions, costs, or new risks:

Current constraint:
Smallest useful next improvement:
Evidence that would disconfirm it:
```

## Meta-Harness Extension

Use this only when the system will create, adapt, evaluate, or govern more than one harness.

```markdown
What the meta-harness operates on:
Target-neutral harness definition:
Supported target bindings:
Meaning that every binding must preserve:

Generation boundary:
- What the generator may decide:
- What must be declared by policy or a human:
- What remains prohibited or unknown:

Evaluation boundary:
- Deterministic structural and policy checks:
- Runtime or end-to-end checks:
- Independent or human review:
- Private or held-out cases:
- Evidence the candidate cannot rewrite:

Version and registry model:
- Definition identity:
- Binding identity:
- Candidate harness identity:
- Evaluator and fixture identity:
- Evidence package identity:

Promotion:
- Required gates:
- Who can approve adoption:
- Rollout boundary:
- Rollback target:
- Reasons to preserve rejection or incomplete state:
```

The canvas describes an engineered pattern, not a native Codex configuration file. Start with one workflow and expand only when the pieces are genuinely reused.
