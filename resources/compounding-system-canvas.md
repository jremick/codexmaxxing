# Compounding System Canvas

Use this for a recurring workflow that may deserve a persistent harness or orchestration system. Leave a field small or mark it `unknown` instead of inventing detail.

```markdown
System objective:
Throughput or outcome unit:
System boundary:
Explicit non-goals:

Intent and authority:
- Who can request a run?
- What may the system read?
- What may it write?
- Which transitions require approval?

Semantic contract:
- Core entities:
- Important relationships:
- Allowed states:
- Invariants:
- Meaning of failure, error, incomplete, and unknown:

Harness:
- Instructions and policies:
- Tools and capabilities:
- Routing rules:
- Required outputs:
- Validation checks:

Orchestration graph:
- Nodes:
- Dependency and control-flow edges:
- State passed between nodes:
- Failure and recovery routes:
- Integration point:

Evidence and observability:
- Required traces or events:
- Artifact provenance:
- Deterministic checks:
- Independent or human checks:
- Data that must not be collected:

Improvement loop:
- Feedback sources:
- Regression suite:
- Candidate-change process:
- Promotion gate:
- Rollback path:
- Counter-metrics:

Current constraint:
Smallest useful next improvement:
Evidence that would disconfirm it:
```

The canvas describes an engineered pattern, not a native Codex configuration file. Start with one workflow and expand only when the contracts are reused.
