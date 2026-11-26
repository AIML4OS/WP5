---
id: L2-IMP-PIPELINES-AND-AUTOMATION
title: "Workflows, pipelines and proportionate automation"
level: 2
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 4.2, 4.3"
relations:
  realises: [L1-IMP-PROCESS-WORKFLOW-AUTOMATION]
  related: [L2-IMP-REPRODUCIBILITY-ENABLERS]
ai_assisted: true
order: 30
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

Workflows operationalise the process. A workflow should make clear how data enters the process, how it is transformed, how models are trained or applied, how outputs are validated and how results are passed on to later production steps. It should define where automation is appropriate and how errors or unexpected results are handled.

**Pipelines** execute processing steps consecutively, so that the output of one step becomes the input of the next. Feedback loops and CI/CD components can support more complex applications.

**Feedback loops** are particularly important: models may be affected by changes in input data, classifications, reporting behaviour, population structures or business rules. Workflows should include mechanisms for evaluating performance over time, detecting drift and deciding when models, pipelines or validation routines need updating.

**Proportionate automation:** well-tested, low-risk steps may be highly automated. In other cases automation should primarily support experts by preparing outputs for review, flagging uncertain cases or providing structured evidence for decisions.
