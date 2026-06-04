# Task Contract Template

Use this when a request is too large or ambiguous to execute safely from a single sentence.

```markdown
Goal:
Source of truth:
Audience or user:
Constraints:
Allowed writes:
Privacy boundary:
Verification:
Stop conditions:
Final answer should include:
```

## Notes

- `Goal` should describe what is true when the work is done.
- `Source of truth` should name the repo, file, issue, doc, live system, or user instruction that wins conflicts.
- `Allowed writes` should say whether local files, remote services, production systems, or GitHub state can be changed.
- `Privacy boundary` should name data or examples that must not appear in outputs.
- `Verification` should name concrete checks.
- `Stop conditions` should prevent risky guessing.
