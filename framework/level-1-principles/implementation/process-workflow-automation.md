---
id: L1-IMP-PROCESS-WORKFLOW-AUTOMATION
title: "Process, workflow and automation"
level: 1
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 4, 7"
relations:
  derives_from: [L0-IMP-PROCESS-MODELS-AND-MLOPS]
  # Section 7 of the paper: "Together, these principles support quality
  # dimensions such as reproducibility, explainability, transparency, and effectiveness."
  supports: [L1-QUA-REPRODUCIBILITY, L1-QUA-EXPLAINABILITY, L1-QUA-EFFECTIVENESS]
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

**Principle:** AI/ML applications in official statistics should be embedded in well-defined statistical and technical workflows, rather than treated as isolated experiments.

This includes integration with regular statistical production and clear process steps for development, validation, deployment, monitoring, maintenance and eventual replacement or retirement of models and related components. Automation should be used to improve consistency, reduce manual error and support efficient and reproducible production.

The appropriate level of automation should be **proportionate** to the use case. It depends on data sensitivity, methodological maturity, production stability, operational risk and the need for human review by statisticians, methodologists or subject-matter experts.
