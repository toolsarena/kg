---
title: "Data management 742"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 747
---

# Data management 742

| Question | Things to consider |
| --- | --- |
| What is the proportion of read queries in
relation to write queries? Would caching be
likely to improve performance? | • Read-heavy workloads can benefit from a
caching layer, like ElastiCache or DAX if the
database is DynamoDB.
• Reads can also be offloaded to read
replicas with relational databases such as
Amazon RDS. |
| Does storage and modification (OLTP -
Online Transaction Processing) or retrieval
and reporting (OLAP - Online Analytical
Processing) have a higher priority? | • For high-throughput read as-is transacti
onal processing, consider a NoSQL
database such as DynamoDB.
• For high-throughput and complex read
patterns (like join) with consistency use
Amazon RDS.
• For analytical queries, consider a columnar
database such as Amazon Redshift or
exporting the data to Amazon S3 and
performing analytics using Athena or
Amazon Quick. |
| What level of durability does the data
require? | • Aurora automatically replicates your data
across three Availability Zones within
a Region, meaning your data is highly
durable with less chance of data loss.
• DynamoDB is automatically replicate
d across multiple Availability Zones,
providing high availability and data
durability.
• Amazon S3 provides 11 nines of durabilit
y. Many database services, such as Amazon
RDS and DynamoDB, support exporting
data to Amazon S3 for long-term retention
and archival. |
