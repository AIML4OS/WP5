---
id: L2-QUA-ACCURACY-ROBUSTNESS-GUIDELINES
title: "Quality guidelines: Accuracy & Robustness (A1-A9)"
level: 2
task: "5.1"
group: quality-guidelines
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.4.1"
relations:
  realises: [L1-QUA-ACCURACY-ROBUSTNESS]
  related: [L2-QUA-QUALITY-GUIDELINES]
ai_assisted: true
order: 10
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.4.1. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

| ID | Guideline | Important building blocks |
|---|---|---|
| A1 | Ensure that machine learning methods follow standard scientific methodology in relation to statistics and AI/ML. Document the methodology used (including reasons for selecting a particular method) and communicate it to the target audience. | Check model assumptions where applicable.<br>Create a methodological protocol document describing each step, decision, and rationale. |
| A2 | Analyse and evaluate the suitability and quality of training data. |  |
| A3 | Perform feature selection. | Compare model performance based on the features used.<br>Describe why each feature was included or removed. |
| A4 | Report relevant metrics along with suitable uncertainty quantification. | Subject matter experts determine relevant accuracy metrics and threshold values for training, evaluation, and quality assurance of AI/ML models.<br>Quantify uncertainty by measures such as confidence intervals, or robustness checks with e.g. a cross-validation approach. |
| A5 | Ensure that the model does not introduce bias or exhibits disproportionately low performance for relevant subgroups. | Subject matter experts specify relevant subgroups.<br>Evaluate accuracy metrics from A4 for relevant subgroups. |
| A6 | Communicate the performance of models transparently to relevant internal stakeholders during model training, evaluation, and use in production. | Produce a summary of accuracy metrics for considered models. |
| A7 | Define the desired object of robustness analyses, e.g., specific predictions, model coefficients, accuracy metrics, or aggregate values of the target variable. | Consider robust AI/ML methods as candidate models.<br>Analyse the effect of deliberate manipulation or the addition of grossly incorrect data points, e.g. by introducing controlled perturbations or synthetic anomalies.<br>Analyse the effect of violating model assumptions and different hyperparameter choices. |
| A8 | Assess the risk of concept drift; if relevant, implement a procedure for detecting concept drift. | Evaluate the model on a ground-truth holdout sample at regular intervals to detect concept drift. If a systematic decrease in performance is observed, initiate retraining or recalibration of the model. |
| A9 | Re-evaluate all guidelines concerning accuracy and robustness for applications to new populations (e.g. another region or country). |  |
