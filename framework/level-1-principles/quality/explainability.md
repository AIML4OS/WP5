---
id: L1-QUA-EXPLAINABILITY
title: "Explainability"
level: 1
task: "5.1"
group: quality-dimension
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.3.2"
  - ref: saidani-dumpert-2025
relations:
  derives_from: [L0-QUA-ESS-QUALITY-FRAMEWORK, L0-QUA-TOWARDS-ML-READY-QF]
  related: [L1-QUA-QUALITY-DIMENSIONS]
ai_assisted: true
order: 20
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.3.2. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

**Short description:** The ability to understand how the results are generated (technically, relationships between variables, meaning of model components).

Quoted literally (!) at the moment from Saidani and Dumpert (2025):

> “Explainability is the ability to understand which relationships the algorithm uses to make predictions, i.e. to be able to demonstrate the (possibly local) relationship between input and output variables - in other words, on the basis of which relationships outputs are generated. Defined in this way, explainability as post-hoc interpretability is becoming more and more relevant in the face of new laws and regulations on the use of artificial intelligence systems (European AI Act). Independently thereof, explainable models are preferable because they generally increase trust among users and allow developers to spot specification mistakes more easily. In addition to post-hoc interpretability, Lipton (2018) widens the concept of explainability to include decomposability and algorithmic transparency. Decomposability is present when the model components have intuitive meanings. This applies in particular to the features and their (estimated) parameters, provided that such a relation exists in a procedure at all. Algorithmic transparency, on the other hand, is present when the behaviour of the algorithm can be described well not in terms of content but rather in technical terms, for example on the basis of convergence or optimality criteria.”

<!-- Source note: the source marks this as 'Quoted literally (!) at the moment'; it contains a LaTeX citation \citet{Lipton.2018}, shown here as 'Lipton (2018)'. -->
