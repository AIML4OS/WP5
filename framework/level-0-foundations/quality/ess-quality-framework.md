---
id: L0-QUA-ESS-QUALITY-FRAMEWORK
title: ESS common quality framework (CoP, QAF, Handbook)
level: 0
task: "5.1"
group: quality-framework
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.1; 'Towards an AI/ML-ready ESS Quality Framework'"
  - ref: es-cop
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

The European Statistical System (ESS) quality policy is anchored in Regulation (EC) No 223/2009 and operationalised through the European Statistics Code of Practice (CoP). The common ESS quality architecture is layered:

- The **CoP** defines the quality principles and indicators.
- The **Quality Assurance Framework (QAF)** translates them into assurance practices.
- Other standards, such as the **ESS Handbook for Quality and Metadata Reports**, give recommendations and guidance on how to collect evidence and report on quality.

Quality of statistical products is assessed along the quality dimensions, not against rigid thresholds. The principle of *fit for purpose* lets user needs determine the appropriate balance between criteria.

## Relevance for AI/ML

According to WP 5.1, the CoP does not need to be replaced; its principles remain the compass for using ML in official statistics. ML changes the quality assurance problem in three ways:

1. **The quality object changes**: training and validation data, trained models, features, hyperparameters, validation design, software environments, monitoring procedures and model versions can significantly influence output quality.
2. **The evidence changes**: standard quality indicators need to be complemented by model-performance metrics, uncertainty estimates, subgroup performance, robustness checks, drift indicators, reproducibility evidence and model-version documentation.
3. **The institutional dimension changes**: methodological control over models, external providers and infrastructure dependencies, skills, MLOps capacity, accountability, confidentiality and human oversight.

In May 2026 the ESSC agreed on a process for revising the CoP, leading to a new version in the course of 2028, with AI identified as one of the drivers for change.
