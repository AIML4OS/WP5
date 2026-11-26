---
id: L2-X-TASK-CONNECTIONS
title: "Connections between quality, methodology and implementation"
level: 2
task: "cross"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 5 'Connections methodology and implementation', Tables 1 and 3, and 'Connection to WP 5.3'"
  - ref: saidani-dumpert-2025
relations:
  related: [L2-X-AI-CARDS]
ai_assisted: true
order: 5
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 5 'Connections methodology and implementation', Tables 1 and 3, and 'Connection to WP 5.3'. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

The connection between Tasks 5.1, 5.2 and 5.3 should not be viewed as merely a sequence of separate contributions, but rather as an integrated framework in which the standards, methods and implementation reinforce each other. In order to harmonise the final output of WP5 and make explicit how legal, methodological, quality-related and technical requirements interact at the use-case level, a bridging framework is needed.

The table below outlines the tasks of WP5 and their interconnections.

## Bridging function of the three WP5 tasks

| WP5 task | Main focus | Contribution to the common framework | Bridge with the other tasks |
|---|---|---|---|
| Task 5.1 | Standards for quality, ethics and legal compliance in statistical production | Defines the quality dimensions, guidelines and legal principles that AI use cases should satisfy | Provides the normative and quality references for methodological choices in Task 5.2 and technical implementation in Task 5.3 |
| Task 5.2 | Methodological framework | Clarifies how models are developed, validated, compared and assessed within statistical use cases | Translates standards from Task 5.1 into methodological procedures and informs implementation needs in Task 5.3 |
| Task 5.3 | Implementation framework | Covers operational deployment, reproducibility, monitoring, maintenance and organizational embedding | Makes the quality and methodological requirements technically actionable and sustainable over time |

According to this interpretation, AI Cards can serve as a shared documentation layer for the three tasks. Rather than creating an additional reporting burden, they can serve as a concise operational interface connecting standards, methods, and implementation. This is particularly pertinent in light of the AI Act, as the documentation, transparency, monitoring and oversight obligations must be translated into operational routines that are comprehensible to both methodological experts and technical teams.

The relevance of this bridging function is particularly evident when considering concrete quality requirements. For instance, robustness and explainability cannot be meaningfully assessed if the relevant tests, metrics, and modelling choices are not documented and retained over time. Similarly, reproducibility depends not only on abstract principles, but also on the existence of versioned code, stable environments, documented data flows, and well-defined procedures for rerunning models. This implies that several quality guidelines developed in WP 5.1 already entail technical and organisational requirements within the remit of WP 5.3. However, their actual application hinges on methodological design choices belonging to WP 5.2.

## Links between the tasks

The link between WP 5.1 and WP 5.2 is particularly important when it comes to methodological decisions that affect the assessment of quality dimensions. For instance, the frequency of model retraining, how subgroup performance is treated, how uncertainty is handled, and whether to opt for more or less interpretable models are not purely technical questions, but rather depend on methodological objectives and quality requirements. Conversely, if WP 5.1 requires explainability, robustness, fairness, or reproducibility, WP 5.2 must specify how these characteristics are assessed in practice and under which assumptions. Similarly, the link between WP 5.2 and WP 5.3 is important, as methodological decisions only become sustainable in production if they are embedded in the right technical and organisational processes. This includes data and model versioning, reproducible pipelines, monitoring routines and criteria for determining when a model change is substantial enough to require renewed validation or documentation. Requirements related to reproducibility, logging, transparency, human oversight, and lifecycle monitoring should be considered when implementation frameworks are designed. In this sense, the bridging section should clarify that compliance with quality standards applies not only to the trained model itself, but also to the production environment, as shown in Table 3.

| Bridge relation | Example | Why it matters |
|---|---|---|
| Task 5.1 ↔ Task 5.2 | Explainability requirement translated into model selection criteria and post-hoc interpretability analyses | Ensures that quality standards are methodologically operationalised |
| Task 5.1 ↔ Task 5.3 | Reproducibility requirement translated into version control, environment management and logging | Ensures that quality requirements remain enforceable in production |
| Task 5.2 ↔ Task 5.3 | Retraining strategy translated into monitoring thresholds, MLOps routines and maintenance schedules | Ensures that methodological assumptions remain valid over time |
| Task 5.1 ↔ Task 5.2 ↔ Task 5.3 | AI Cards used as common documentation artefact across design, validation and deployment | Creates a shared operational language and reduces fragmentation across the work package |

In practical terms, this suggests that the final WP5 output would benefit from a common template or, at the very least, a harmonised set of documentation fields to be used across the different tasks. This template does not need to be overly rigid, but it should explicitly state the minimum information required to judge whether a given AI use case is methodologically sound, technically feasible, legally compliant, and consistent with the quality standards proposed in WP 5.1. This kind of bridging approach also supports coherence with the broader legal and governance perspective developed in the AI Act section. If documentation, monitoring and oversight are already required for compliance purposes, the same information should also, where possible, serve quality assessment, methodological validation and implementation governance. This reduces duplication and increases the practical usability of the framework for NSIs. Overall, the purpose of the bridging section is not to create an additional framework alongside those developed in the three tasks, but to make their interdependencies explicit and operational. In this sense, the bridge between WP5 tasks provides a way to connect standards, methods and implementation in a coherent architecture that is understandable at the level of individual use cases and compatible with legal, quality and organisational requirements in official statistics.

## Connection to WP 5.3 (still to be agreed with WP 5.3)

> Quoted literally (!) at the moment from Saidani and Dumpert (2025): “Standardised data processing and data management are essential for quality: The evaluation of accuracy is facilitated immensely by tools that output relevant quality metrics and their variance during model training by default. Ensuring robustness and explainability can be extremely time-consuming if specific tests and evaluation routines are not pre-programmed and easily accessible. Standardised processes, once developed, also allow for better timeliness and higher efficiency. In order to ensure that data, codes and environments are reproducible, certain procedures and technical tools must be established and used across the whole organisation. Practices and processes that aim to reliably and efficiently develop, productively deploy, manage, monitor and maintain machine learning models are summarised under the term “machine learning operations” (MLOps) (Kreuzberger 2022). To the extent that such processes, tools and practices are necessary to fulfil the quality dimensions specified in the quality frameworks of official statistics, MLOps is also a basic prerequisite for machine learning in official statistics. Consequently, it is essential that MLOps is given ample consideration during the development of IT platforms and data management systems. As part of the ONS-UNECE-ML-2022 project, requirements for MLOps systems and possible system architectures have been gathered and evaluated (Engdahl 2022).”

WP 5.3 addresses the question of the extent to which AI/ML really introduces something new into the statistical production process or whether existing approaches, regulations and best practices should simply be transferred, albeit from a more technical perspective. So can (and should) AI/ML be integrated into already existing processes, or are there fundamental differences? If AI/ML is viewed as mostly non-parametric statistical methods, there will be no fundamental differences (as Yung et al. (2022) already recognised when they named their document QF4SA, i.e. ‘for statistical algorithms’ instead of ‘for AI/ML’). But are there differences from a technical or organisational (‘who is doing what in a modern statistical office?’) perspective? To what extent do DevOps/MLOps aspects differ in principle from previous approaches? And what impact does this have on compliance with quality guidelines, for example on (model) reproducibility, reproducible analytical pipelines, or on the question of when it is even worthwhile to build your own pipeline for AI/ML? Finally, the question of how to deal with the fact that not all models will be created or trained in-house at the NSI in future, but that external models will also be used in statistics production in GSBPM phases 4 to 6, for example in the form of large language models, will be addressed.

<!-- Source notes: Responsible for writing: Marco (5.2) / Pina, Renato (5.1), Florian (5.3); reviewing: Martin, Jens. The quote contains LaTeX citations \citep{Kreuzberger.2022} and \citep{Engdahl.2022}, shown here as plain text. -->
