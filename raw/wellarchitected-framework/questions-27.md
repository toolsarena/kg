---
title: "Questions"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 739
---

# Questions

• PERF 3. How do you store, manage, and access data in your workload?
PERF 3. How do you store, manage, and access data in your workload?
The optimal data management solution for a particular system varies based on the kind of data
type (block, file, or object), access patterns (random or sequential), required throughput, frequency
of access (online, offline, archival), frequency of update (WORM, dynamic), and availability and
durability constraints. Well-Architected workloads use purpose-built data stores which allow
different features to improve performance.
