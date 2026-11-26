---
id: L1-QUA-ETHICAL-RISKS
title: "Ethical risks and their coverage by existing frameworks"
level: 1
task: "5.1"
group: ethics
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 3.6"
relations:
  derives_from: [L0-QUA-ETHICAL-FOUNDATIONS, L0-QUA-LEGAL-FRAMEWORK]
  related: [L1-QUA-ETHICAL-PRINCIPLES]
ai_assisted: true
order: 55
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 3.6. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

As can be seen in the previous section, many statistical offices and organisations have developed frameworks, guidelines and principles for the ethical use of AI. Building on approaches such as that developed by Destatis and reflecting recurring themes in the literature, some key ethical risks in the use of AI/ML for official statistics can be identified as:

- Production of false statistics: Errors arising from AI/ML applications may lead to inaccurate outputs or conclusions, potentially resulting in incorrect decisions by data

users. From a societal perspective, this is obviously harmful and needs to be avoided, if possible.

- Reinforcement of unwanted bias: AI systems may amplify pre-existing biases in training data and under-represented groups may be systematically misclassified or overlooked, leading to distorted aggregates.
- Creation of “transparent” citizens: A transparent citizen is one who is very visible to the state, for example people whose interactions with the state generate dense, frequent, linkable data trails. Extensive data linkage facilitated by AI may increase the risk of these individuals becoming overly visible to the state, raising concerns about privacy and proportionality.
- Transfer of responsibility to an algorithm and lack of transparency: Opaque AI processes may undermine human oversight and make it difficult to challenge or review decisions if documentation and traceability are insufficient.
- Disclosure of sensitive information: It is obviously harmful and incompatible with the public's perception of official statistics if data which requires protection (due to statistical law, data protection requirements, confidentiality obligations or any other standard) becomes publicly known. Breaches of confidentiality, whether through inadequate safeguards or misuse of AI, would severely damage public trust and may have legal consequences.
- Lack of environmental sustainability: Certain AI models, particularly deep learning systems and large language models, require substantial computational resources, with significant energy and water consumption etc., especially during training phases. It is considered desirable, from an environmental point of view, that AI would not generate excessive usage.

The question that needs to be considered is whether these AI-related ethical risks need to be addressed specifically or whether the existing quality and legal frameworks are sufficient to adequately counter them, possibly with adaption. The European quality framework applies throughout the ESS, as does European law (and national law, although it should be acknowledged that there may be differences between countries of course) and NSIs are also guided by the FPOS and the European CoP.

If ethical risks cannot be fully addressed by existing quality frameworks and legal requirements (European and national), then additional ethical requirements might have to be elaborated in a separate ethical framework for AI/ML usage in the production of official statistics. Alternatively, the legal requirements at European or national level should be adapted as required. An examination of the six risks indicates the following:

## Production of false statistics

Existing quality frameworks already require sound statistical methodology and accuracy. AI introduces specific technical challenges but does not create fundamentally new quality concerns beyond the scope of established standards.

## Unwanted bias

Fairness and representativeness criteria are already embedded within existing quality requirements. Statistical systems are (or should be) designed to ensure balanced and accurate representation across subgroups.

## Creation of the "transparent" citizen

In many jurisdictions, legal provisions explicitly restrict re-identification and regulate data linkage. Confidentiality and data protection principles under the CoP and statistical laws also mitigate this risk. For example, the reidentification of a person after the deletion of identifying features (such as name or address) or after the aggregation of individual data is prohibited under section 21 of the German Federal Statistics Act while the linking statistical data is also comprehensively regulated in section 13a of the Federal Statistics Act.

## Transfer of responsibility to an algorithm and lack of transparency

Legal accountability for its actions remains with the relevant statistical authority, even where processes are automated. GDPR also provides safeguards against completely automated decision-making, and institutional review mechanisms should ensure oversight. For example, the general quality assurance framework for official statistics states that “the heads of the National Statistical Institutes and of Eurostat and, where appropriate, the heads of other statistical authorities have the sole responsibility for deciding on statistical methods, standards and procedures, and on the content and timing of statistical releases”. In some countries, if an algorithm executes a process step it must still be possible to reconstruct or document essential steps of the activity, otherwise it could lead to a situation where it is no longer possible to conduct a judicial review of official activities (for example, Article 19 (4) of the Basic Law for Germany) or where oversight bodies such as parliaments could no longer effectively monitor administrative action (for example, Article 20 (3) of the Basic Law for Germany).

## Disclosure of sensitive information

Article 20 (4) of the European Statistics Regulation requires statistical offices and other national authorities and the Commission (Eurostat) to take all necessary regulatory, administrative, technical and organisational measures within their respective spheres of competence to ensure the physical and logical protection of confidential data. If personal data are processed, no matter what the tool used, this may only be done on a specific and appropriate legal basis and for statistical purposes only.

## Lack of environmental sustainability

This area receives comparatively little attention in existing legal and quality frameworks and may require greater explicit consideration.

## Overall assessment

Overall, apart from environmental sustainability, most of the risks associated with AI usage are already covered by established quality and legal frameworks or these frameworks can be adapted to do so. Criteria such as accuracy, fairness, confidentiality and accountability obligations apply regardless of the methodology employed by the statistical office. For example, accuracy requirements address the risk of false statistics, fairness and representativeness are embedded in quality standards, profiling and re-identification are prohibited under statistical and data protection law and accountability remains legally vested in the statistical authority, even in automated processes.
