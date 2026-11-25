---
id: L1-QUA-ACCURACY-ROBUSTNESS
title: "Accuracy & Robustness"
level: 1
task: "5.1"
group: quality-dimension
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Sections 2.3, 2.3.1"
relations:
  derives_from: [L0-QUA-ESS-QUALITY-FRAMEWORK]
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

**Short description:** The phenomenon of interest is described correctly, with stable but useful results despite small perturbations, and the model performs well across different groups, i.e. it is fair in a descriptive sense.

**Accuracy** refers to the proximity of an estimated or predicted value to its true value. Which quantity it refers to (individual entries, aggregates, population parameters) and which metric is used (e.g. F1, MSE, distribution distances) is decided per use case. Accuracy includes *descriptive fairness*: for all subgroups defined in advance by subject matter experts, sufficient accuracy is achieved. Sampling-based uncertainties are also part of accuracy and must be measured, evaluated and reported.

**Robustness** means that models continue to provide useful results despite minor changes in the data-generating process, e.g. concept drift, assumptions that no longer apply, or deliberate application to a new population.

WP 5.1 merges accuracy and robustness, following Yung et al. (2022); Saidani et al. (2023) had separated them.
