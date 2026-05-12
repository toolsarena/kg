---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 963
---

# Common anti-patterns:

• You do not identify data assets with similar characteristics (such as sensitivity, business criticality,
or regulatory requirements) that are being processed or stored.
• You have not implemented a data catalog to inventory your data assets.
Benefits of establishing this best practice: Implementing a data classification policy allows you to
determine the most energy-efficient storage tier for data.
Level of risk exposed if this best practice is not established: Medium


# Common anti-patterns:

• You assume that all workloads have similar data storage and access patterns.
• You only use one tier of storage, assuming all workloads fit within that tier.
• You assume that data access patterns will stay consistent over time.