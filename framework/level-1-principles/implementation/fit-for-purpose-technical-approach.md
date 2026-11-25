---
id: L1-IMP-FIT-FOR-PURPOSE
title: "Fit-for-purpose technical approach"
level: 1
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 5, 7"
relations:
  derives_from: [L0-IMP-PROCESS-MODELS-AND-MLOPS]
  # Section 7 of the paper: "Together, these principles support quality
  # dimensions such as reproducibility, explainability, transparency, and effectiveness."
  supports: [L1-QUA-REPRODUCIBILITY, L1-QUA-EXPLAINABILITY, L1-QUA-EFFECTIVENESS]
ai_assisted: true
order: 20
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

**Principle:** The technical approach for an AI/ML application should be fit for its intended statistical purpose and proportionate to the requirements of the use case.

Choices concerning architecture, hosting environments, APIs, applications, data pipelines, frameworks, tools, integrations and MLOps components should be guided by statistical needs, data sensitivity, reproducibility, maintainability, security and organisational capabilities.

A fit-for-purpose approach does not imply using the most advanced or complex technology available. Simpler and more transparent solutions may be preferable if they meet the methodological and quality requirements with lower operational risk, lower maintenance burden and better long-term sustainability.
