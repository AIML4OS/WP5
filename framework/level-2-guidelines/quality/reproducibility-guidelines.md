---
id: L2-QUA-REPRODUCIBILITY-GUIDELINES
title: "Quality guidelines: Reproducibility (R1-R3)"
level: 2
task: "5.1"
group: quality-guidelines
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.4.3"
  - ref: wp51-quality-guidelines-working
    locator: "Earlier version of the same checklist"
relations:
  realises: [L1-QUA-REPRODUCIBILITY]
ai_assisted: true
order: 30
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

Use as a checklist: for each application, record a status per guideline (*completed/observed*, *not completed/not observed*, *not relevant* with justification) and review it periodically over the lifecycle (WP 5.1, Section 2.4).

| ID | Guideline | Important building blocks |
|---|---|---|
| R1 | Ensure that random data splits, e.g. into train/test/validation sets, can be reproduced from the data. | Set a random seed for data splitting processes. |
| R2 | Ensure that parameter estimation is made reproducible. | Set random seeds in all relevant algorithms. |
| R3 | Ensure that predictions are reproducible. | Ensure that prediction results can be regenerated under the same conditions. |

<!-- Review note: the earlier working document had six reproducibility guidelines (P1-P6) on archiving data and code, access, codebooks, software versions and code comments. They are not in the current version; Task 5.1 to confirm whether they moved elsewhere (e.g. to Task 5.3). -->
