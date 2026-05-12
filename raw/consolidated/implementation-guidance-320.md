---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 147
---

# Implementation guidance

Begin by identifying all of the elements of your workload that require instrumentation. Once all
components are accounted for, leverage tools such as AWS X-Ray and OpenTelemetry to gather
trace data for analysis with tools like X-Ray and Amazon CloudWatch ServiceLens Map. Engage
in regular reviews with developers, and supplement these discussions with tools like Amazon
DevOps Guru, X-Ray Analytics and X-Ray Insights to help uncover deeper findings. Establish alerts
from trace data to notify when outcomes, as defined in the workload monitoring plan, are at risk.
