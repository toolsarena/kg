---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 926
---

# Implementation guidance

To have the most cost-efficient workload, you must regularly review the workload to know if there
are opportunities to implement new services, features, and components. To achieve overall lower
costs the process must be proportional to the potential amount of savings. For example, workloads
that are 50% of your overall spend should be reviewed more regularly, and more thoroughly, than
workloads that are five percent of your overall spend. Factor in any external factors or volatility.
If the workload services a specific geography or market segment, and change in that area is
predicted, more frequent reviews could lead to cost savings. Another factor in review is the effort
to implement changes. If there are significant costs in testing and validating changes, reviews
should be less frequent.
Factor in the long-term cost of maintaining outdated and legacy, components and resources and
the inability to implement new features into them. The current cost of testing and validation may
exceed the proposed benefit. However, over time, the cost of making the change may significantly
increase as the gap between the workload and the current technologies increases, resulting in even
larger costs. For example, the cost of moving to a new programming language may not currently
be cost effective. However, in five years time, the cost of people skilled in that language may
increase, and due to workload growth, you would be moving an even larger system to the new
language, requiring even more effort than previously.
Break down your workload into components, assign the cost of the component (an estimate
is sufficient), and then list the factors (for example, effort and external markets) next to each
component. Use these indicators to determine a review frequency for each workload. For example,
you may have webservers as a high cost, low change effort, and high external factors, resulting
in high frequency of review. A central database may be medium cost, high change effort, and low
external factors, resulting in a medium frequency of review.
Define a process to evaluate new services, design patterns, resource types, and configurations to
optimize your workload cost as they become available. Similar to performance pillar review and
