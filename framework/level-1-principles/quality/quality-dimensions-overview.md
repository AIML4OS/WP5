---
id: L1-QUA-QUALITY-DIMENSIONS
title: "Quality dimensions for AI/ML in official statistics (overview)"
level: 1
task: "5.1"
group: quality-dimension
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.3"
  - ref: saidani-dumpert-2025
  - ref: saidani-et-al-2023
  - ref: yung-et-al-2022
relations:
  derives_from: [L0-QUA-ESS-QUALITY-FRAMEWORK, L0-QUA-TOWARDS-ML-READY-QF]
ai_assisted: true
order: 5
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.3. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

The use of machine learning in the production of official statistics is typically motivated by the ability to improve current practice with respect to efficiency and quality. AI/ML methods are often used to reduce manual labour for data processing tasks such as coding, imputation, and editing (e.g., UNECE 2021). In such cases, possible gains include reduced costs, i.e., increased cost efficiency, increased accuracy, and improved timeliness. The use of AI/ML for similar processes may also lead to, e.g., reduced respondent burden because of the utilization of new data sources and improvements in reproducibility from increased standardization. The possible gains from using AI/ML in official statistics can be described in terms of the principles given in the CoP and QAF. See Saidani et al. (2023) for a deeper discussion on the relation between the CoP and AI/ML.

In many respects, we follow the suggestions and descriptions made by Saidani and Dumpert (2025) regarding quality dimensions. They propose accuracy, robustness, explainability, reproducibility, timeliness and punctuality, and cost-effectiveness as quality dimensions and supported them by corresponding quality guidelines. We adopt this approach but suggest modifying the quality dimensions to better reflect why AI/ML is used in official statistics. Thus, this approach not only considers the ideal ‘how’, but also elaborates on aspects of the ‘why’ by adding the quality dimension of effectiveness.

Further changes compared to Saidani and Dumpert (2025) include the merging of the quality dimensions accuracy and robustness, the omission of the dimension timeliness and punctuality, and the explicit inclusion of fairness as a separate quality dimension. On closer inspection, the merging of accuracy and robustness is a reunification. Yung et al. (2022) list these two dimensions as one joint dimension. Saidani et al. (2023) elevated robustness to a separate quality dimension in order to emphasize the stability of the techniques used. The reversal is therefore less a substantive measure than a communicative one.

The removal of the dimension of timeliness and punctuality follows from its overlap with the corresponding QAF dimension. In addition, the introduction of the new quality dimension of effectiveness (which does not only include cost-effectiveness) addresses this aspect.

Finally, the inclusion of fairness as a separate quality dimension is logical if one follows the reasoning of Saidani et al. (2023) and Saidani and Dumpert (2025), i.e., to consider the impact on individuals and population subgroups. Instead of treating fairness as an overarching aspect, the dimension is given its own quality guidelines and must be considered directly (and not only indirectly, as in earlier proposals).

In the following, we refer to Saidani and Dumpert (2025) for the quality dimensions already developed, describe them here only in short, and only elaborate on the new ones in more detail. See Table XX for an overview of the quality dimensions.

| Dimension | Short description |
|---|---|
| Accuracy & Robustness | The phenomenon of interest is described correctly, with stable but useful results despite small perturbations and the ability of the model to perform well across different groups, i.e. to be fair in a descriptive sense. |
| Explainability | The ability to understand how the results are generated (technically, relationships between variables, meaning of model components). |
| Reproducibility | The results of the model can be identically reproduced. |
| Effectiveness | The cost effectiveness, added value, and proportionality of the model are well understood. |

<!-- Review note (Task 5.1): the text announces 'the explicit inclusion of fairness as a separate quality dimension' with its own guidelines, but the table has no separate Fairness dimension (fairness is part of Accuracy & Robustness) and Section 2.4 has no fairness guidelines. 'Table XX' is not yet numbered. -->
