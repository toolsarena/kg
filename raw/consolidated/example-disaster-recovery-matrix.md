---
title: "Example disaster recovery matrix"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 681
---

# Example disaster recovery matrix

For each workload, investigate and understand the impact of downtime and lost data on your
business. The impact typically grows with downtime and data loss, but the shape of the impact
can differ based on the workload type. For example, downtime for up to an hour might have low
impact, but after that, the impact could quickly intensify. Impact can take many forms, including
financial impact (such as lost revenue), reputational impact (including loss of customer trust),
operational impact (such as a missed payroll or decreased productivity), and regulatory risk. Once
completed, assign the workload to the appropriate tier.
Consider the following questions when you analyze the impact of failure:
1. What is the maximum time the workload can be unavailable before unacceptable impact to the
business is incurred?
2. How much impact, and what kind, will be incurred by the business by a workload disruption?
Consider all kinds of impact, including financial, reputational, operational, and regulatory.
3. What is the maximum amount of data that can be lost or unrecoverable before unacceptable
impact to the business is incurred?
4. Can lost data be recreated from other sources (also known as derived data)? If so, also consider
the RPOs of all source data used to recreate the workload data.
5. What are the recovery objectives and availability expectations of workloads that this one
depends on (downstream)? Your workload's objectives must be achievable given the recovery
capabilities of its downstream dependencies. Consider possible downstream dependency
workarounds or mitigations that can improve this workload's recovery capability.
