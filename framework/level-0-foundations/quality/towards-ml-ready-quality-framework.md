---
id: L0-QUA-TOWARDS-ML-READY-QF
title: "Towards an AI/ML-ready ESS quality framework"
level: 0
task: "5.1"
group: quality-framework
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 'Towards an AI/ML-ready ESS Quality Framework' (after Section 2.4)"
  - ref: es-cop
relations:
  related: [L0-QUA-ESS-QUALITY-FRAMEWORK]
ai_assisted: true
order: 15
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 'Towards an AI/ML-ready ESS Quality Framework' (after Section 2.4). Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

The European Statistics Code of Practice (CoP) is the main pillar of the ESS Common Quality Framework. As such, the Code is meant to be both robust, withstanding institutional, technological and societal changes over time, and flexible, reflecting evolving user needs, methodological advances and innovation.

In May 2026, the European Statistical System Committee (ESSC) agreed on a process for revising the CoP. This should lead to a new version in the course of 2028 reflecting the new realities of developing, producing and disseminating European statistics. Artificial intelligence has been identified as one of the drivers for change. The revision of the CoP will subsequently feed into the other components of the ESS common quality framework, following a top-down approach ensuring coherence and strategic alignment. AI/ML is indubitably transforming how data are collected, processed, disseminated and used. AI techniques can improve efficiency, timeliness, accuracy and relevance. At the same time, its growing role raises questions about transparency, accountability, data protection and methodological soundness. The impact of AI therefore extends across the three pillars of the CoP: institutional environment, statistical processes and statistical outputs.

## Why machine learning changes the quality assurance problem

The European Statistics Code of Practice does not need to be replaced. Its principles remain the compass to implement ML techniques for the production of Official Statistics. Professional independence, sound methodology, statistical confidentiality, accuracy, coherence, relevance and clarity all remain essential and relevant [ref]. However, ML changes the quality assurance problem in three important ways. First, the quality object changes. Quality assurance no longer concerns only institutions, source data, statistical methods, production processes and final outputs. Training and validation data, trained models, features, model hyper parameters, validation design, software environments, monitoring procedures and model versions can influence significantly output quality. Second, the evidence changes. Standard quality indicators need to be complemented by model-performance metrics, uncertainty estimates, subgroup performance, robustness checks, drift indicators, reproducibility evidence and model-version documentation. Third, the institutional dimension changes. ML introduces questions about methodological control over models, external providers and infrastructure dependencies, skills, MLOps capacity, accountability, confidentiality and human oversight. Quality assurance must therefore extend across model training, selection, validation, deployment, monitoring, retraining and reproduction.

## Pathways to an AI/ML-ready ESS common quality framework

First, the existing CoP principles remain valid, but their meaning needs to be specified for ML. For example, Principle 12 on accuracy and reliability needs to encompass ML performance metrics, uncertainty, subgroup performance and robustness. Principle 8 on appropriate statistical procedures, for example, could require procedures to detect performance degradation or concept drift and trigger retraining or recalibration. Under Principle 7, sound methodology should encompass model choice, assumptions, feature selection, training-data quality, explainability and reproducibility. Under Principle 14, coherence and comparability encompass model stability over time, generalisability and concept drift. Under Principle 15, accessibility and clarity encompass explainability, interpretability and transparency of model outputs. Second, the supporting layers of the quality framework, i.e. the QAF and the Handbook providing reporting methodological guidance, meta data standards and quality indicators need to be extended to cover the ML-specific concepts.

## The contribution of AIML4OS WP5

AIML4OS WP5 provides important conceptual, methodological and operation input for this evolution. Its purpose is not to create a separate quality system. It provides the raw material to make the existing ESS quality architecture ML-ready.

At the CoP level, WP5 quality dimensions contribute to specifying existing principles. These include accuracy and robustness, explainability, reproducibility, generalisability and beneficiality. For instance, explainability through model interpretability and algorithmic transparency become and important component of Principle X on Accessibility and Clarity. Reproducibility implies specific requirement for statistical procedures derived from ML lifecycle management involving data splits, seeds, code, libraries, parameters and prediction environments (ref to StatOps]. Drift monitoring addresses model degradation, concept drift, retraining and recalibration. Beneficiality contributes to Principle X on Cost efficiency making explicit that the use of ML should demonstrate benefits compared with existing production methods.

At the QAF level, WP5 provides guidelines, checklists, controls and ways of working to ensure quality throughout the process. These make abstract concepts verifiable: Was training-data quality assessed? Was subgroup performance checked? Were uncertainty estimates reported? Is drift monitored? Can the model and its results be reproduced?

For evidence reporting, WP5 contribute to identify what should be documented and how: model purpose, training data, validation results, limitations, monitoring arrangements and human oversight. It can identify relevant ML metadata such as model type and version, training data, validation design, monitoring arrangements and retraining information. Finally, it will provide ML-specific evidence such as performance metrics, uncertainty, subgroup behaviour, robustness, drift and benefit indicators for key statistical production ML use cases .

## Conclusions

ML creates real opportunities to improve the quality of European statistics. It also puts pressure on the existing quality framework. This is not because its fundamental principles have become obsolete. Rather, ML introduces new quality objects and concepts and new evidence is required to operationalise the CoP principles The CoP therefore remains the overarching normative framework. The main challenge is to contextualise its principles and indicators and extend the supporting quality-assurance instruments where necessary.Its concepts, principles, guidelines, methodologies, checklists, metadata requirements, indicators and use-case feedback can provide concrete input to the future revision of the ESS quality framework.

<!-- Review note (Task 5.1): this section names the WP5 quality dimensions as 'accuracy and robustness, explainability, reproducibility, generalisability and beneficiality', while Section 2.3 uses Accuracy & Robustness, Explainability, Reproducibility and Effectiveness. Principle numbers are still 'Principle X' in two places. -->
