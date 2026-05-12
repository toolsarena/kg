---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 759
---

# AWS Well-Architected Framework Framework

• Implement strategies to improve the query performance. Some of the key strategies include:
• Using a columnar file format (like Parquet or ORC).
• Compressing data in the data store to reduce storage space and I/O operation.
• Data partitioning to split data into smaller parts and reduce data scanning time.
• Partitioning data in Athena
• Partitions and data distribution
• Data indexing on the common columns in the query.
• Use materialized views for frequent queries.
• Understanding materialized views
• Creating materialized views in Amazon Redshift
• Choose the right join operation for the query. When you join two tables, specify the larger
table on the left side of join and the smaller table on the right side of the join.
• Distributed caching solution to improve latency and reduce the number of database I/O
operation.
• Regular maintenance such as vacuuming, reindexing, and running statistics.
• Experiment and test strategies in a non-production environment.
