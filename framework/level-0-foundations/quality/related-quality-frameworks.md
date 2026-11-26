---
id: L0-QUA-RELATED-QUALITY-FRAMEWORKS
title: "Similar approaches: earlier ESS quality guidelines"
level: 0
task: "5.1"
group: quality-framework
status: draft
example: true
owners: []
reviewers: []
sources:
  - ref: wp51-final-2026-10
    locator: "Section 2.2"
  - ref: reinert-et-al-2016
  - ref: de-waal-et-al-2019
  - ref: kowarik-et-al-2020
  - ref: kowarik-et-al-2025
relations:
  related: [L0-QUA-ESS-QUALITY-FRAMEWORK]
ai_assisted: true
order: 20
---

> **Example content.** Text reproduced from the WP 5.1 final document (version of 29.10.2026), Section 2.2. Only the layout was changed (line breaks, lists, tables). Not yet reviewed by Task 5.1.

The approach to adapt or extend the CoP is not new. Quality guidelines for multi-source statistics primarily address challenges of the quality of input data (Reinert et al., 2016) and its integration as well as the quality of the output data (De Waal et al., 2019). The guidelines are organized around the quality assessment of administrative data as a new data source, with special attention to linkage errors, coverage problems, and measurement of inconsistencies. Input data is evaluated along the standard quality dimensions such as accuracy, timeliness, coherence, comparability, and cost-efficiency. The quality of output data can be covered by the definition of Quality Measures and Computation Methods (QMCMs), which are formal descriptions of how quality indicators (e.g., mean squared error under classification error) are calculated for different multi-source settings (De Waal et al., 2019). Some of the defined settings are multiple non-overlapping cross-sectional microdata sets, multiple cross-sectional microdata sets with overlapping variables and units between different data sets, or with multiple non-overlapping cross-sectional microdata sets under-coverage of the target population. In total, they define six such settings. These frameworks thus provide a detailed account of how input data quality propagates to output quality in multi-source environments.

The ESSnet Big Data II guidelines (Kowarik et al., 2020) are structured along a three-phase production process structure—input, throughput I, and throughput II—focusing on data acquisition and transformation. The input phase includes accreditation procedures for new, often privately owned data sources to ensure that they are fit for use within official statistics, considering cost, efficiency, and reliability. It considers all possible impacts of the adoption of a new data source on the producer of official statistics. These guidelines are split into guidelines for privately-owned data (e.g. MNO data) and data where no cooperation with the data owner is necessary to gain access to the raw data (e.g. web data). The throughput phase I addresses data processing at a lower level, describing quality aspects such as coverage, comparability over time, measurement error, model error, and processing error. These are elaborated for specific classes of big data, including mobile network (MNO), earth observation, AIS, web, and social media data. Throughput phase II then outlines quality checks for the use of derived statistical data, such as validation against traditional sources, survey replacement, and flash estimates, but deliberately omits the output phase, assuming that dissemination processes remain unchanged.

Similarly, the WIN project guidelines for web-scraped data (Kowarik et al., 2025) adopt the same three-phase structure (input, throughput I, throughput II) and focus heavily on data source stability and consistency. The input phase defines both general and use-case-specific guidelines for assessing the relevance, stability, and persistence of web sources (e.g., job advertisements). Throughput I covers linking, coverage, and comparability errors, while Throughput II mirrors the big data guidelines with validation and calibration recommendations. Additional guidelines address the design of a centralized web data infrastructure, highlighting the need for technical and organizational coherence when managing dynamic online data sources.

Across all these frameworks, quality is conceptualized primarily as a property of data and data processing workflows, focusing on input and output data, with limited consideration of intermediate modelling steps.

The frameworks from previous ESSnet projects focus on GSBPM phases 2 Design, 3 Build, 4 Collect, 5 Process and provided in a limited way input for 6 Analyse - being like the output phase in the aforementioned production model. The machine learning (AI/ML) quality guidelines being developed here take a different perspective. The usage of a model can happen in all GSBPM phases. While earlier guidelines emphasize how to transform new or complex data into usable statistical input, the AI/ML-oriented approach extends quality considerations to the model training, estimation, and prediction process, as well as to the IT infrastructure and reproducibility.

Rather than rewriting existing statistical quality frameworks, the AI/ML guidelines build upon and complement them, shifting the emphasis from data quality to model quality. The quality dimensions therefore are made up of model accuracy and robustness, explainability, bias and explainability, and reproducibility of results. These dimensions are adapted to ensure that statistical outputs derived through machine learning are interpretable, stable, and methodologically sound.

In summary, while traditional and big data quality frameworks are data-centric, addressing challenges of acquisition, integration, and validation, the emerging AI/ML quality framework is model-centric, ensuring that once high-quality data are available, the analytical and predictive processes producing the final outputs are traceable, reproducible, and trustworthy. Together, these complementary perspectives complete the quality coverage across the full GSBPM cycle—from data input to model-based output dissemination.
