---
id: L2-X-AI-CARDS
title: "AI Cards as a shared documentation layer"
level: 2
task: "cross"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 5, Table 2"
  - ref: golpayegani-2024
relations:
  realises: [L1-QUA-LEGAL-AI-ACT]
  related: [L2-X-TASK-CONNECTIONS, L2-QUA-AI-ACT-OPERATIONAL-MAPPING, L2-IMP-SYSTEM-LEVEL-TRANSPARENCY, L2-IMP-MODEL-REGISTRIES]
ai_assisted: true
order: 10
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 5, Table 2. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

As previously discussed, structured documentation can support the implementation of AI Act requirements in statistical processes. A comprehensive approach that can also be adopted in official statistics is based on AI cards (Golpayegani D. et al., 2024). AI Cards offer a concise yet thorough approach to documenting the intended use of AI, data sources, model components, human involvement, risk profile, lifecycle changes and applicable legal and quality requirements. They can therefore serve as a bridge between legal compliance under the AI Act, the methodological assessment in WP5.2, the quality requirements in WP5.1 and the implementation aspects in WP5.3.

The AI Cards framework, as proposed in recent literature on AI Act-aligned documentation, provides a suitable candidate for this bridging role. AI Cards provide a holistic structure for documenting the key elements of an AI implementation within a specific use case. From the perspective of WP 5.1, the main added value of such a framework lies in linking abstract quality standards and legal requirements to specific implementation choices. From the perspective of WP 5.2, the framework provides a place where methodological assumptions, validation choices, and model-related decisions can be documented in a standardised, comparable manner. From the perspective of WP 5.3, the framework creates a bridge to technical implementation, monitoring, retraining and maintenance procedures, including those related to MLOps and the use of external or third-party models.

The bridging role is therefore crucial in clarifying the minimum documentation artefacts required for the integration of AI systems into statistical production. One practical approach to addressing this issue is to define a common set of information elements that should be documented for each use case. The AI Cards approach provides this structure and can be adapted to the needs of official statistics. As an example, the following table provides an overview of the potential use of AI components to bridge WP5 tasks.

| AI Cards component | Description | Main relevance for WP5 |
|---|---|---|
| General information | Use case name, responsible unit, GSBPM phase/subphase, type of statistics, status | Connects the use case to the scope and standards of Task 5.1 and to the organisational context of Task 5.3 |
| Intended use | Statistical objective, role in the business process, expected impact on individuals or businesses | Links beneficiality, proportionality and legal/ethical relevance across Tasks 5.1 and 5.2 |
| Key components | Model type, features, preprocessing pipeline, technical dependencies | Connects methodological choices in Task 5.2 with implementation constraints in Task 5.3 |
| Data and processing | Data sources, training/validation/test split, data quality controls, linkage constraints | Supports quality assessment in Task 5.1 and methodological validation in Task 5.2 |
| Human involvement | Role of experts, validation workflow, oversight and override mechanisms | Links AI Act and governance requirements with methodological review and operational deployment |
| Risk profile | Main risks identified, FRIA/DPIA if relevant, AI Act category | Bridges legal compliance, ethical analysis and use-case level assessment |
| Quality | Indicators structured along the quality dimensions and guidelines | Directly operationalises Task 5.1 and creates measurable links to Tasks 5.2 and 5.3 |
| Lifecycle and changes | Retraining strategy, monitoring, substantial modifications, retirement criteria | Connects robustness, drift monitoring and maintenance processes across the three tasks |
| Regulation and compliance | Relevant AI Act provisions, links to CoP/QAF principles and internal procedures | Ensures coherence between legal obligations and existing ESS governance processes |

This mapping also helps to clarify some of the feedback received regarding the quality checklist. There is a need for more operational guidance on uncertainty assessment, drift monitoring, governance and documentation from various perspectives. Introducing a bridging layer based on common information elements allows these requirements to be explicitly linked to ongoing methodological and technical work, rather than remaining at an abstract level.
