---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 875
---

# Implementation guidance

Workload components, which are designed to deliver business value to the organization, may
encompass various services. For each component, one might choose specific AWS Cloud services
to address business needs. This selection could be influenced by factors such as familiarity with or
prior experience using these services.
After identifying your organization's requirements as mentioned in COST05-BP01 Identify
organization requirements for cost, perform a thorough analysis on all components in your
workload. Analyze each component considering current and projected costs and sizes. Consider
the cost of analysis against any potential workload savings over its lifecycle. The effort expended
on the analysis of all components of this workload should correspond to the potential savings or
improvements anticipated from optimization of that specific component. For example, if the cost
of the proposed resource is $10 per month, and under forecasted loads would not exceed $15 per
month, spending a day of effort to reduce costs by 50% (five dollars per month) could exceed the
potential benefit over the life of the system. Use a faster and more efficient data-based estimation
to create the best overall outcome for this component.
Workloads can change over time, and the right set of services may not be optimal if the workload
architecture or usage changes. Analysis for selection of services must incorporate current and
future workload states and usage levels. Implementing a service for future workload state or usage
may reduce overall costs by reducing or removing the effort required to make future changes. For
example, using EMR Serverless might be the appropriate choice initially. However, as consumption
