---
id: L0-IMP-PROCESS-MODELS-AND-MLOPS
title: Process models and engineering practice (GSBPM, CRISP-DM, MLOps)
level: 0
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 1, 4.1"
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

The implementation principles are derived from established practices in statistical production, software engineering, data engineering and MLOps.

- **GSBPM** (an ESS standard since 2017) describes the phases and subprocesses of statistical production and is useful for positioning where AI/ML is used. It does not specifically support development, deployment, monitoring and maintenance of AI/ML applications.
- **CRISP-DM** is the de facto industry standard process for ML and AI projects, with six phases: Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation and Deployment. It may be adopted for pre-trained models such as LLMs, and may be extended with a lifecycle perspective.
- **MLOps** provides concepts, tools and practices for managing the ML lifecycle (data preparation, training, validation, deployment, monitoring, retraining, maintenance). Its concepts need to be interpreted in relation to statistical production, confidentiality, quality frameworks and GSBPM.
- **StatOps** is used in the paper for a possible operational layer for statistical production that takes inspiration from MLOps but applies more broadly to official statistics.
