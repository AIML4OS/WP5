---
id: L2-X-AI-CARDS
title: "AI Cards as a shared documentation layer"
level: 2
task: cross
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 5 'Connections methodology and implementation', Tables 1-3; Section 4, Table 1"
  - ref: golpayegani-2024
relations:
  realises: [L1-QUA-LEGAL-AI-ACT]
  related: [L2-IMP-SYSTEM-LEVEL-TRANSPARENCY, L2-IMP-MODEL-REGISTRIES]
ai_assisted: true
order: 10
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

AI Cards (Golpayegani et al., 2024) document the intended use of AI, data sources, model components, human involvement, risk profile, lifecycle changes and applicable legal and quality requirements. In the WP 5.1 draft they are proposed as a bridge between legal compliance (AI Act), the quality requirements of Task 5.1, the methodological assessment of Task 5.2 and the implementation aspects of Task 5.3.

| AI Cards component | Description | Main relevance for WP5 |
|---|---|---|
| General information | Use case name, responsible unit, GSBPM phase, type of statistics, status | Scope and standards (5.1); organisational context (5.3) |
| Intended use | Statistical objective, role in the business process, expected impact | Beneficiality, proportionality, legal/ethical relevance (5.1, 5.2) |
| Key components | Model type, features, preprocessing pipeline, technical dependencies | Methodological choices (5.2) and implementation constraints (5.3) |
| Data and processing | Data sources, train/validation/test split, data quality controls, linkage constraints | Quality assessment (5.1) and methodological validation (5.2) |
| Human involvement | Role of experts, validation workflow, oversight and override | AI Act and governance; methodological review; deployment |
| Risk profile | Main risks, FRIA/DPIA if relevant, AI Act category | Legal compliance, ethical analysis |
| Quality | Indicators along the quality dimensions and guidelines | Operationalises 5.1; links to 5.2 and 5.3 |
| Lifecycle and changes | Retraining, monitoring, substantial modifications, retirement criteria | Robustness, drift monitoring, maintenance across tasks |
| Regulation and compliance | AI Act provisions, links to CoP/QAF, internal procedures | Coherence with ESS governance |

The source suggests that the final WP5 output would benefit from a common template, or at least a harmonised set of documentation fields, stating the minimum information needed to judge whether a use case is methodologically sound, technically feasible, legally compliant and consistent with the quality standards.
