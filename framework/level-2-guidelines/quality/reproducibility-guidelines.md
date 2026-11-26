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
relations:
  realises: [L1-QUA-REPRODUCIBILITY]
  related: [L2-QUA-QUALITY-GUIDELINES]
ai_assisted: true
order: 30
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.4.3. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

| ID | Guideline | Important building blocks |
|---|---|---|
| R1 | Ensure that random data splits, e.g. into train/test/validation sets, can be reproduced from the data. | Set a random seed for data splitting processes. |
| R2 | Ensure that parameter estimation is made reproducible. | Set random seeds in all relevant algorithms. |
| R3 | Ensure that predictions are reproducible. | Ensure that prediction results can be regenerated under the same conditions. |

<!-- Review note (Task 5.1): the earlier 'Quality guidelines working document' had six reproducibility guidelines (P1-P6: archiving data and code, unchanged archives, future access, dataset description and codebook, software and versions, code comments). They are not in this version; confirm whether they were dropped or moved. -->
