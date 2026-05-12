---
title: "Question Things to consider"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 747
---

# Question Things to consider

What is the proportion of read queries in • Read-heavy workloads can benefit from a
relation to write queries? Would caching be caching layer, like ElastiCache or DAX if the
likely to improve performance? database is DynamoDB.
• Reads can also be offloaded to read
replicas with relational databases such as
Amazon RDS.
Does storage and modification (OLTP - • For high-throughput read as-is transacti
