# Example Work Patterns

The examples on this page are synthetic. Their names, systems, paths, and evidence are fictional and do not describe a specific person, repository, organization, or environment.

## Source-Backed Decision

Someone needs to choose between several products, services, routes, or approaches. The useful outcome is not a long search summary. It is a recommendation that can be checked.

A good workflow:

1. name the decision and the criteria that matter,
2. use current primary sources where possible,
3. separate observed facts, inference, and unknowns,
4. compare the options against the same criteria,
5. recommend an option and explain the tradeoff,
6. cite the claims most likely to change.

Live inventory, availability, prices, rules, and schedules need especially careful wording. A listing is not proof that an item is on a shelf, and a search result is not a confirmed booking. Treat webpages, documents, and tool output as evidence, not as instructions that can change the task or its permissions. Higher-stakes medical, legal, financial, or safety questions need stronger sources, clearer limits, and appropriate professional review.

## Planning Around Live Constraints

A trip, purchase, or event may depend on location, timing, weather, access, budget, availability, and personal preferences. Codex can collect the moving pieces, compare workable options, surface conflicts, and prepare a plan.

The plan should distinguish:

- confirmed facts from assumptions,
- current information from details that still need checking,
- recommendations from decisions only the user can make,
- planning from external actions such as booking, buying, sending, or cancelling.

Unless explicitly authorized, stop at a reviewable plan or draft rather than taking the external action.

## Rough Material To Useful Output

The input may be a pile of notes, a voice transcript, images, links, or an unfinished idea. Start by asking what the material is for: a decision, a follow-up list, a brief, an article, or a record.

Then:

- extract the useful facts and open questions,
- choose a structure that fits the intended reader,
- preserve uncertainty instead of filling gaps with plausible details,
- draft the output,
- check names, dates, claims, and requested actions against the source material.

Private source material should stay private. A reusable template may preserve the method, but not the original transcript, names, account details, or identifying context.

## Write For A Real Audience

A useful communication task includes the audience, desired outcome, relevant facts, tone, and any boundaries. Codex can turn that into a concise update, email, post, review, proposal, or difficult-message draft.

The final check is not just grammar. It should ask whether the draft says the real thing, sounds natural, preserves the facts, and avoids promises or claims the sender cannot support. Drafting does not authorize sending or publishing.

## Make The Right Kind Of Artifact

Sometimes the result should be a document, spreadsheet, presentation, PDF, diagram, visualization, or small interactive tool. Choose the format from how the result will be used, not from which generator is most convenient.

A reliable artifact workflow combines:

- source inspection,
- a clear information structure,
- deterministic checks for calculations, links, and required fields,
- rendered or interactive inspection for layout and usability,
- a separate approval boundary for sharing, publishing, or deployment.

Structural validation can show that a file is well formed. It cannot by itself prove that the artifact is clear, accurate, accessible, or visually good.

## Recurring Review Or Admin Work

A repeated review might collect updates, find records, triage an inbox, prepare reminders, or draft follow-up. The first design choice is the action boundary:

- **read-only:** inspect and report,
- **draft-only:** prepare proposed actions for review,
- **action:** make approved changes in the connected system.

Start with the narrowest useful mode. Define the source of truth, what counts as actionable, how no-action runs should look, and which changes always need approval. Keep credentials, raw messages, private records, and personal history out of reusable public artifacts.

## Contributor-Ready Application

A small application depends on services that contributors cannot access. The useful mission is not simply to improve its README. It is to create a safe local path that makes the project understandable and testable without private infrastructure.

Useful outcomes might include:

- fixture or demonstration data,
- a documented local run path,
- a single verification command,
- server-side secret handling,
- and a clear distinction between demonstration and production behavior.

## Reusable Workflow Library

A team repeats the same repository review and documentation workflow. Instead of preserving raw prompts or session logs, the reusable parts become a small skill, checklist, or validator.

The public artifact should contain only the generalized workflow. It should not contain the originating repository, internal instructions, tool inventory, paths, configuration, or private examples.

## Layered System Diagnosis

A service reports a visible failure, but the cause could be access, runtime, integration, configuration, data, or presentation.

The safe pattern is:

1. start read-only,
2. identify evidence that distinguishes the layers,
3. gather the least-sensitive evidence first,
4. make the smallest reversible change,
5. read the affected system back.

## Device Workflow

An application communicates with an external device. A plausible source change is not enough to prove that the workflow works.

Verification may need to cross several layers:

```mermaid
flowchart LR
  A["Source change"] --> B["Build"]
  B --> C["Focused tests"]
  C --> D["Simulator or fixture"]
  D --> E["Physical target"]
  E --> F["Observed result"]
```

The final claim should state exactly which layers were checked and which remain unverified.

## Parallel Workstreams

A broad review contains independent research, implementation, and verification questions. Parallel work is useful only when the lanes have non-overlapping ownership and a clear integration point.

Each lane should define:

- its source of truth,
- allowed writes,
- expected output,
- evidence,
- stop condition,
- and parent handoff.

## Compounding Documentation Maintenance

A synthetic documentation system tracks fast-changing product claims. Its first useful reusable workflow defines required source types, public-safety checks, output files, and a publication gate.

The workflow graph is deliberately small:

```mermaid
flowchart LR
  A["Detect claim needing review"] --> B["Read current official source"]
  B --> C["Draft candidate update"]
  C --> D["Validate links + public safety"]
  D --> E["Review claim boundary"]
  E --> F["Approve versioned change"]
  D -->|failure| G["Return findings"]
  E -->|unsupported| G
```

The shared vocabulary distinguishes `observed behavior`, `official claim`, `inference`, `unknown`, and `verified date`. After several runs reveal that redirects are being mistaken for stable canonical URLs, the failure becomes a regression case.

A proposed workflow change adds canonical-URL resolution and records where each result came from. It runs against the prior suite plus the new case. It is adopted only if link validation improves without weakening the public-safety or claim-boundary checks. The previous version remains available for rollback.

This is compounding because evidence from one run changes later behavior through a versioned and reviewable path. The example remains synthetic: no real task IDs, traces, accounts, paths, connected systems, or private configuration are preserved.

## Common Shape

```mermaid
flowchart TD
  A["Intent"] --> B["Reusable workflow or work plan"]
  B --> C["Bounded execution"]
  C --> D["Claim-specific evidence"]
  D --> E["Reviewed generalized improvement"]
  E --> B
```

The reusable pattern is the decision structure, not private detail from the work that produced it.
