---
id: L1-QUA-EFFECTIVENESS
title: "Effectiveness"
level: 1
task: "5.1"
group: quality-dimension
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.3.4"
  - ref: yung-et-al-2022
  - ref: saidani-et-al-2023
  - ref: saidani-dumpert-2025
relations:
  derives_from: [L0-QUA-ESS-QUALITY-FRAMEWORK, L0-QUA-TOWARDS-ML-READY-QF]
  related: [L1-QUA-QUALITY-DIMENSIONS]
ai_assisted: true
order: 40
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.3.4. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

**Short description:** The cost effectiveness, added value, and proportionality of the model are well understood.

Yung et al. (2022) introduce the cost effectiveness quality dimension and describe this dimension in terms of the costs associated with the use of AI/ML and corresponding calculations for evaluating cost efficiency, e.g., they propose the ratio of accuracy to incurred costs as a metric. Saidani et al. (2023) and Saidani and Dumpert (2025) further elaborate on the dimension on, e.g., the importance of understanding the requirements for an AI/ML application before such calculations are made.

However, because AI/ML applications are used at NSIs to achieve multiple gains, it is beneficial to expand on this dimension when evaluating and comparing the advantages of AI/ML methods. We hence propose the Effectiveness quality dimension, which encompasses cost effectiveness, added value for statistics and statistical production, and proportionality.

Note that, we do not describe how each of the possible benefits should be measured or compared to other approaches. For such calculations, we refer to e.g. Saidani et al. (2023), Saidani and Dumpert (2025), Yung et al. (2022), and UNECE (2021) and the references therein.

## Cost effectiveness

The cost effectiveness quality dimension was proposed in Yung et al. (2022) and further elaborated in Saidani et al. (2023) and Saidani and Dumpert (2025). Yung et al. (2022) describe fixed and ongoing costs for machine learning and relate the performance of an AI/ML application, primarily with respect to accuracy, to the total costs incurred. They also offer guidance on organizational considerations and describe possibilities for cost reduction from AI/ML. Saidani et al. (2023) and Saidani and Dumpert (2025) expand on the dimension by, e.g. introducing other possible advantages from using AI/ML applications such as improved timeliness and enabling of additional analyses.

Cost efficiency from using AI/ML can be achieved by reducing manual labour in processing tasks such as coding and editing. Supervised AI/ML models trained on annotated data can then replace manual labour for parts of the incoming material. In addition, unsupervised models may be utilized in e.g. anomaly detection tasks which may be suitable for editing. Cost reduction is also possible by facilitating new data sources by using AI/ML. Such cases include very large data sets unsuitable for standard tools and data with non-numeric formats such as text and images, the use of which require AI/ML processing.

Cost effectiveness calculations require careful consideration of various circumstances both on the case level and on the NSI level. Following Saidiani et al. (2023), it is recommended that calculations for cost effectiveness should rely on the established procedures of an NSI.

## Added value

As noted in Statistics Canada’s Framework for Responsible Machine Learning Processes (REF), AI/ML applications may result in added value for statistical products or in greater efficiency in the production process. Such values may include improvements in quality as described by the other AI/ML quality dimensions or by the ESS QAF.

The accuracy of results produced using an AI/ML application can be improved compared to previous methods (e.g., UNECE 2021, Yung et al. 2018). In addition, using AI/ML in statistical production can also improve the ability to describe accuracy, as AI/ML applications may be more systematic than earlier approaches. Timeliness may also be improved by AI/ML applications (e.g., UNECE 2021). In this context, timeliness should be understood as the time required for the processing in which AI/ML is applied, i.e., the GSBPM process step.

The CoP Principle 9 on Non-Excessive Burden on Respondents states that other data sources should be used whenever possible, and that data sharing and integration should be promoted to minimise response burden. Because AI/ML methods are indispensable tools when utilizing alternative data sources, e.g. in text coding and processing of non-tabular formats (Saidani et al. 2023, Saidani and Dumpert 2025, Yung et al. 2018), the use of AI/ML may contribute to reduced response burden.

AI/ML applications can also reduce response burden by simplifying data collection. For example, real-time coding of open text responses by AI/ML may facilitate accurate responses while reducing time spent by respondents and improving respondent experience. In addition, the dimension may describe improvements in e.g. reproducibility, standardization, and visualization of results.

## Proportionality

It is often the case that there exist multiple AI/ML solutions which fulfil the quality requirements of an AI/ML application. They will however often differ in e.g. model complexity, computational demand, data use, and deployment configuration. In such situations, it is proposed to adhere to the principle of parsimony, i.e., “Occam’s razor”, which applied to the case of AI/ML in official statistics promotes selection of a simpler model before more intricate models with respect to multiple characteristics. In the context of effectiveness, the principle supports using models which fulfils quality criteria avoiding more complex models to increase added value.

<!-- Source note: '(REF)' for the Statistics Canada framework and the spelling 'Saidiani' are as in the source. -->
