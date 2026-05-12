---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 960
---

# Common anti-patterns:

• You assume that all workloads have similar data storage and access patterns.
• You only use one tier of storage, assuming all workloads fit within that tier.
• You assume that data access patterns will stay consistent over time.
• Your architecture supports a potential high data access burst, which results in the resources
remaining idle most of the time.
Benefits of establishing this best practice: Selecting and optimizing your architecture based on
data access and storage patterns will help decrease development complexity and increase overall
utilization. Understanding when to use global tables, data partitioning, and caching will help you
decrease operational overhead and scale based on your workload needs.
Level of risk exposed if this best practice is not established: Medium
