---
id: L2-IMP-TECHNICAL-ARCHITECTURE-HOSTING
title: "Technical architecture and hosting choices"
level: 2
task: "5.3"
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Section 5"
relations:
  realises: [L1-IMP-FIT-FOR-PURPOSE]
  related: []
ai_assisted: true
order: 40
---

> **Example content** seeded from the WP5 working documents during repository setup. The text is taken from the cited sources and has not yet been reviewed by the task group.

The technical architecture should be designed in relation to the role the AI/ML application plays in the statistical process. Relevant choices include hosting environment, application layer, API setup, data pipeline design, model deployment pattern, evaluation and monitoring tools, security controls and integration with existing systems.

**Governability** is central: an application should be possible to understand, control, monitor and change in a structured way (e.g. model registries, controlled APIs, access management, logging, environment management, dependency tracking, validation workflows).

**Hosting:** models and components may be hosted on-premises, in cloud environments or in hybrid setups. The choice depends on data sensitivity, legal requirements, scalability, cost, latency, available infrastructure and the level of control needed. For sensitive data, local or controlled environments may be necessary.

**Generative AI:** the architecture must consider how context is supplied (system prompts, prompt templates, RAG, vector databases, metadata repositories, classification systems). Outdated or poorly governed context reduces output quality.

**Tool integrations and agents:** the architecture must define clear boundaries for what the system can do, with access rights, logging, validation, approval steps and fallback procedures.

Technical design should start early, as part of deciding whether a use case is feasible and can be moved into regular production.
