---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 859
---

# Implementation steps

• Define workload outcomes: Meet with the stakeholders in the business and define the outcomes
for the workload. These are a primary measure of customer usage and must be business metrics
and not technical metrics. There should be a small number of high-level metrics (less than five)
per workload. If the workload produces multiple outcomes for different use cases, then group
them into a single metric.
• Define workload component outcomes: Optionally, if you have a large and complex workload,
or can easily break your workload into components (such as microservices) with well-defined
inputs and outputs, define metrics for each component. The effort should reflect the value
and cost of the component. Start with the largest components and work towards the smaller
components.
