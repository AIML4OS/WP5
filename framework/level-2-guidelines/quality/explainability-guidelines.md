---
id: L2-QUA-EXPLAINABILITY-GUIDELINES
title: "Quality guidelines: Explainability (E1-E3)"
level: 2
task: "5.1"
group: quality-guidelines
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.4.2"
  - ref: wp51-quality-guidelines-working
    locator: "Earlier version of the same checklist"
relations:
  realises: [L1-QUA-EXPLAINABILITY]
ai_assisted: true
order: 20
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

Use as a checklist: for each application, record a status per guideline (*completed/observed*, *not completed/not observed*, *not relevant* with justification) and review it periodically over the lifecycle (WP 5.1, Section 2.4).

| ID | Guideline | Important building blocks |
|---|---|---|
| E1 | Determine the desired level of explainability, in particular whether decomposability, algorithmic transparency or interpretability of the results are required, and whether additional requirements arise from the legal situation for the given statistics. | |
| E2 | Evaluate AI/ML methods in terms of their explainability. Use only methods that fulfil the requirements from E1. If two models yield approximately similar results, use the more explainable model. | Record and justify model changes, distinguishing methodological updates from real-world effects. Log decision-relevant information during prediction for later inspection. |
| E3 | Carry out post-hoc explainability analyses if necessary. | Apply post-hoc analysis tools. Document how explanations were generated and how they were validated or reviewed by experts. |
