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
  - ref: wp51-quality-guidelines-working
    locator: "Earlier version of the same checklist"
relations:
  realises: [L1-QUA-ACCURACY-ROBUSTNESS]
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

Use as a checklist: for each application, record a status per guideline (*completed/observed*, *not completed/not observed*, *not relevant* with justification) and review it periodically over the lifecycle (WP 5.1, Section 2.4).

| ID | Guideline | Important building blocks |
|---|---|---|
| A1 | Ensure that machine learning methods follow standard scientific methodology in relation to statistics and AI/ML. Document the methodology used (including reasons for selecting a particular method) and communicate it to the target audience. | Check model assumptions where applicable. Create a methodological protocol document describing each step, decision and rationale. |
| A2 | Analyse and evaluate the suitability and quality of training data. | |
| A3 | Perform feature selection. | Compare model performance based on the features used. Describe why each feature was included or removed. |
| A4 | Report relevant metrics along with suitable uncertainty quantification. | Subject matter experts determine relevant accuracy metrics and threshold values. Quantify uncertainty, e.g. confidence intervals or cross-validation-based robustness checks. |
| A5 | Ensure that the model does not introduce bias or exhibit disproportionately low performance for relevant subgroups. | Subject matter experts specify relevant subgroups. Evaluate the A4 metrics for those subgroups. |
| A6 | Communicate the performance of models transparently to relevant internal stakeholders during training, evaluation and use in production. | Produce a summary of accuracy metrics for considered models. |
| A7 | Define the desired object of robustness analyses, e.g. specific predictions, model coefficients, accuracy metrics or aggregate values of the target variable. | Consider robust AI/ML methods as candidates. Analyse the effect of deliberate manipulation or grossly incorrect data points. Analyse the effect of violating model assumptions and of different hyperparameter choices. |
| A8 | Assess the risk of concept drift; if relevant, implement a procedure for detecting concept drift. | Evaluate the model on a ground-truth holdout sample at regular intervals; if performance decreases systematically, initiate retraining or recalibration. |
| A9 | Re-evaluate all guidelines concerning accuracy and robustness for applications to new populations (e.g. another region or country). | |
