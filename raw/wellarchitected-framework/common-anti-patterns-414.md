---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 750
---

# Common anti-patterns:

• You only use one storage type, such as Amazon EBS, for all workloads.
• You use provisioned IOPS for all workloads without real-world testing against all storage tiers.
• You are not aware of the configuration options of your chosen data management solution.
• You rely solely on increasing instance size without looking at other available configuration
options.
• You are not testing the scaling characteristics of your data store.
Benefits of establishing this best practice: By exploring and experimenting with the data store
configurations, you may be able to reduce the cost of infrastructure, improve performance, and
lower the effort required to maintain your workloads.
Level of risk exposed if this best practice is not established: Medium
