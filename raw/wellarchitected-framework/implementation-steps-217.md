---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 915
---

# Implementation steps

• Analyze existing workload data: Analyze data from the existing workload, previous versions of
the workload, or predicted usage patterns. Use Amazon CloudWatch, log files and monitoring
data to gain insight on how workload was used. Analyze a full cycle of the workload, and collect
data for any seasonal changes such as end-of-month or end-of-year events. The effort reflected
in the analysis should reflect the workload characteristics. The largest effort should be placed on
high-value workloads that have the largest changes in demand. The least effort should be placed
on low-value workloads that have minimal changes in demand.
• Forecast outside influence: Meet with team members from across the organization that can
influence or change the demand in the workload. Common teams would be sales, marketing, or
business development. Work with them to know the cycles they operate within, and if there are
any events that would change the demand of the workload. Forecast the workload demand with
this data.
