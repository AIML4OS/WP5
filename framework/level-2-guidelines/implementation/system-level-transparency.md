---
id: L2-IMP-SYSTEM-LEVEL-TRANSPARENCY
title: "System-level transparency"
level: 2
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Section 3"
relations:
  realises: [L1-QUA-EXPLAINABILITY, L1-IMP-HUMAN-IN-THE-LOOP]
  related: [L2-QUA-EXPLAINABILITY-GUIDELINES]
ai_assisted: true
order: 20
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

CoP Principle 6 requires that European statistics are developed, produced and disseminated in a transparent manner. This also applies to the processes, technical frameworks and components used in production.

Model-level explainability needs to be complemented by **system-level transparency**: the ability to understand an AI/ML-supported output also depends on whether data flows, preprocessing steps, model versions, APIs, hosting arrangements, orchestration tools, logging, monitoring and human review procedures can be described and understood. Without this, it is difficult to distinguish statistical change from technical or operational change.

For generative AI and LLMs, the configuration of the complete AI system, including how context is supplied and how outputs are checked, needs to be transparent enough to support review and auditability.

Open and well-documented components can support transparency, but open source does not by itself guarantee it. Transparency also has an organisational dimension: it should be clear which roles are responsible for model selection, data preparation, validation, deployment, monitoring, approval and maintenance.
