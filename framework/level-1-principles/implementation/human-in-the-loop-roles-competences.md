---
id: L1-IMP-HUMAN-IN-THE-LOOP
title: "Human-in-the-loop, roles and competences"
level: 1
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 6, 7"
relations:
  derives_from: [L0-IMP-PROCESS-MODELS-AND-MLOPS]
  # Section 7 of the paper: "Together, these principles support quality
  # dimensions such as reproducibility, explainability, transparency, and effectiveness."
  supports: [L1-QUA-REPRODUCIBILITY, L1-QUA-EXPLAINABILITY, L1-QUA-EFFECTIVENESS]
ai_assisted: true
order: 30
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

**Principle:** AI/ML applications in official statistics should be designed with clear human involvement, accountability and role allocation throughout the lifecycle.

Human-in-the-loop arrangements are safeguards against errors and a way to maintain statistical insight into production processes where AI/ML is used. It should be clear where human judgement enters the process and how this judgement is documented.

Human involvement can take different forms depending on use case and risk:

- **in the loop**: a human reviews or approves each AI/ML-supported output;
- **on the loop**: humans monitor the system and intervene on anomalies, low confidence or unexpected changes;
- **over the loop**: governance roles or expert groups review the overall use of AI/ML and approve changes.

Implementation also requires shared ways of working and competences across statisticians, methodologists, subject-matter experts, data scientists, data engineers, IT and security specialists.
