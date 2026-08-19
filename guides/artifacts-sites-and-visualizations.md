# Artifacts, Sites, And Visualizations

Choose the output surface from how the result will be reviewed and used, not only from its source material.

## Output Decision

| Desired result | Use |
| --- | --- |
| Document, spreadsheet, presentation, or PDF | Artifact workflow with format-specific review. |
| Interactive chart, map, diagram, calculator, or simulation | Visualization, when available. |
| Hosted website, application, or game | Site. |
| Repository-native application | Ordinary code workflow, with browser or runtime verification as needed. |

## Artifacts

For file-producing tasks, state the expected file type, structure, source data, and review criteria. A generated file is not complete until it has been opened or rendered in an appropriate viewer.

The desktop app can preview supported documents, presentations, spreadsheets, PDFs, and some HTML files. CLI and IDE workflows can create files but do not provide the same visual preview surface, so they should report output paths and the checks performed.

## Visualizations

Use a visualization when interaction materially improves understanding:

- controls change the result,
- time or motion matters,
- spatial relationships matter,
- several variables need exploration.

Prefer a normal table or static diagram when interactivity adds no value. Visualization rendering is not supported in Codex CLI or the IDE extension, and availability remains dependent on product rollout.

## Sites

Sites creates and hosts web experiences. Saving and deploying are different actions.

Every Sites deployment URL is a production deployment. Save a version without deploying when review should happen before publication. The CLI can edit and test a compatible local project but does not provide the standalone Sites management view.

Treat deployment as an external write. Verify the intended content, data boundary, authentication assumptions, and production URL after publication.

## Review Contract

```markdown
Output type:
Intended audience:
Required structure:
Source data:
Visual or interactive checks:
Privacy constraints:
Publication boundary:
Definition of done:
```

## Claim Limits

- File validity does not prove visual fidelity.
- A render does not prove accessibility conformance.
- A local preview does not prove a deployed Site.
- Generated calculations should be checked deterministically.
- Publication requires explicit authority beyond permission to create files.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Artifacts](https://learn.chatgpt.com/docs/artifacts-viewer), [Visualizations](https://learn.chatgpt.com/docs/visualizations), and [Sites](https://learn.chatgpt.com/docs/sites).
