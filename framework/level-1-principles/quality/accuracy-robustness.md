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
    locator: "Section 2.3.1"
relations:
  derives_from: [L0-QUA-ESS-QUALITY-FRAMEWORK, L0-QUA-TOWARDS-ML-READY-QF]
  related: [L1-QUA-QUALITY-DIMENSIONS]
ai_assisted: true
order: 10
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.3.1. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

**Short description:** The phenomenon of interest is described correctly, with stable but useful results despite small perturbations and the ability of the model to perform well across different groups, i.e. to be fair in a descriptive sense.

The dimension Accuracy & Robustness comprises the mathematically-statistically expected quality dimensions. Accuracy in this context refers to the proximity of an estimated or predicted value to its true value. At this level, it is intentionally left open to which size or sizes Accuracy refers (possible examples here include individual entries in datasets, aggregated values, population parameters) and according to which metric Accuracy should be measured (examples here include F1 measures, MSE, or distribution distances). Such specifications are to be decided according to the needs for the respective use case. Accuracy also includes descriptive fairness: For all subgroups that have been defined by subject matter experts in advance (e.g., economic sectors, regions), sufficient accuracies are to be achieved, i.e., no subgroup is processed insufficiently accurately by the KI/ML procedure. Sampling-based uncertainties are also part of Accuracy, which must be adequately measured, evaluated in terms of their relevance, and reported.

The second dimension included here, Robustness, means that models continue to provide useful results despite of minor changes in the data-generating process (and the data to be processed) and are thus generalizable in this sense. The changes can result from the underlying population changing itself (e.g., over time; keyword: concept drift), that assumptions originally made no longer applying, or that a model is deliberately applied to an entirely new population (but robustness does of course not require that every model can be applied everywhere).
