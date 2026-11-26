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
relations:
  realises: [L1-QUA-EXPLAINABILITY]
  related: [L2-QUA-QUALITY-GUIDELINES]
ai_assisted: true
order: 20
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.4.2. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

| ID | Guideline | Important building blocks |
|---|---|---|
| E1 | Determine the desired level of explainability – in particular, whether decomposability, algorithmic transparency, or interpretability of the results are required, and whether additional requirements arise from the legal situation for the given statistics. |  |
| E2 | Evaluate AI/ML methods in terms of their explainability. Use only those AI/ML methods that fulfil the requirements from E1. If two models yield (approximately) similar results, use the more explainable model. | Record and justify model changes, distinguishing between changes due to methodological updates and changes reflecting real-world effects.<br>Implement mechanisms that log decision-relevant information during prediction, enabling later inspection of how outputs were produced. |
| E3 | Carry out post-hoc explainability analyses if necessary. | Apply post-hoc analysis tools to interpret model behaviour.<br>Document how explanations were generated and how they were validated or reviewed by experts. |
