---
id: L2-QUA-AI-ACT-OPERATIONAL-MAPPING
title: "Operational mapping of AI Act requirements to NSI use cases and ESS processes"
level: 2
task: "5.1"
group: legal
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 4, Tables 1 and 2"
relations:
  realises: [L1-QUA-LEGAL-AI-ACT]
  related: [L2-QUA-ACCURACY-ROBUSTNESS-GUIDELINES, L2-QUA-REPRODUCIBILITY-GUIDELINES, L2-QUA-EXPLAINABILITY-GUIDELINES, L2-X-AI-CARDS]
ai_assisted: true
order: 70
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 4, Tables 1 and 2. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

## Operational mapping between AI Act requirements and typical NSI use cases

In addition to this approach, it would be helpful to supplement the general legal overview with an operational map, showing the relationship between typical statistical AI use cases and the relevant AI Act requirements. This can help NSIs to translate legal obligations into practical documentation, thereby ensuring transparency and effective monitoring and oversight of production processes. The following table illustrates how the requirements of the AI Act can be translated into useful documentation for process tracking in relation to a specific use case.

| AI Act requirement | Typical NSI use case | Link with proposed quality checklist | Possible documentation, monitoring and oversight measures |
|---|---|---|---|
| Data governance and data quality (Art. 10) | Imputation, classification, editing based on training data | Accuracy/Robustness: A4 on training data quality, A6 on relevant metrics and uncertainty estimates, A7 on subgroup checks | Documentation of data sources, data lineage, training-validation-test splits, subgroup performance checks, and periodic review of data suitability |
| Technical documentation and record-keeping (Arts. 11–12) | Any operational AI system used in production | Reproducibility: R1–R3; Explainability: E1 on required explainability level | Versioning of code, models and parameters; logging of model changes; retention of model cards or AI Cards; documentation of assumptions and processing steps |
| Transparency and provision of information | Chatbots, AI-assisted respondent interaction, AI-supported outputs | Explainability: E1–E3 | Clear disclosure to respondents or users; labelling of AI-assisted interactions; explanation of the role played by AI in the process |
| Human oversight (Art. 14) | Collaborative AI systems in editing, anomaly detection or coding | Governance-related quality checks; validation by subject-matter experts; review of beneficiality and appropriateness | Human-in-the-loop validation workflow, override procedures, escalation rules, assignment of responsibility to methodological or quality committees |
| Monitoring and post-deployment review | Models reused over time in production | Accuracy/Robustness: A9 on robustness, A13 on reassessment in new settings; Fairness/Generalisability: F1–F2 on subgroup bias and concept drift | Periodic performance reassessment, drift detection, retraining strategy, incident logging, review of substantial changes during the lifecycle |

Although NSIs primarily operate under the GDPR and other data protection frameworks, the AI Act introduces additional legal and operational obligations when AI systems are used in ways that could have a significant impact on individuals’ rights or access to services. Crucially, NSIs must determine which risk category their AI use cases, such as predictive models and large language models, fall into. Although scientific research is generally exempt, operational AI applications used in official statistics — especially those that influence public policy — must be subject to regulatory compliance checks. NSIs should therefore establish internal procedures to map AI systems against AI technical requirements, evaluate risk levels, and ensure alignment with both the AI Act and existing privacy legislation. Where possible, these procedures should be embedded within existing ESS governance structures, rather than being handled separately. Documentation requirements can be integrated into existing methodological protocols and quality reporting. Monitoring obligations can be addressed through regular model review, drift detection, and performance reassessment. Oversight obligations can be assigned to existing methodological, quality, or governance committees. This approach is consistent with the broader view that AI-related legal and ethical safeguards should be incorporated into established statistical governance wherever feasible.

## Interaction between AI Act requirements and existing ESS quality and governance processes

| AI Act area | Current ESS framework | Consistency between frameworks |
|---|---|---|
| Risk management | Existing methodological review, quality assurance procedures, risk-based assessment traditions within NSIs | A compliance checklist makes risk-related issues operational through documented checks on robustness, subgroup performance, fairness and model limitations |
| Documentation and traceability | Quality reports, methodological documentation, audit trails, reproducibility standards | Reproducibility and explainability guidelines and technical documentation can extend existing documentation practices without creating a separate reporting track |
| Human oversight and accountability | Existing governance bodies, methodological committees, quality committees, internal approval processes | Oversight requirements can be integrated into existing validation and approval workflows, including clear role allocation and escalation procedures |
| Monitoring and lifecycle review | Periodic quality review, model maintenance, revision and process monitoring | Lifecycle-oriented monitoring through drift checks, retraining strategies, reassessment in new settings and documentation of substantial changes |
| Transparency | Dissemination metadata, quality reports, respondent information and internal communication practices | Explainability requirements and transparency obligations can be reflected in user-facing disclosures, metadata and quality reporting |

Additionally, validating the practical relevance of the proposed methodological framework against concrete AIML4OS use cases would be beneficial. Testing the quality dimensions and guidelines against ongoing project examples would help to assess their applicability, identify possible gaps also in relation to AI Act compliance, and refine the operational mapping between legal, quality, and methodological requirements. This would keep the standard sufficiently broad for use across different NSIs and use cases.

<!-- Review note (Task 5.1): Table 1 refers to guideline numbers that do not match the checklist in Section 2.4 (e.g. A4 is uncertainty there but 'training data quality' here; A13 and F1-F2 do not exist in Section 2.4). -->
