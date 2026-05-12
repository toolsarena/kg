---
title: "Online Transaction Processing) or retrieval onal processing, consider a NoSQL"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 747
---

# Online Transaction Processing) or retrieval onal processing, consider a NoSQL

and reporting (OLAP - Online Analytical database such as DynamoDB.
Processing) have a higher priority?
• For high-throughput and complex read
patterns (like join) with consistency use
Amazon RDS.
• For analytical queries, consider a columnar
database such as Amazon Redshift or
exporting the data to Amazon S3 and
performing analytics using Athena or
Amazon Quick.
What level of durability does the data • Aurora automatically replicates your data
require? across three Availability Zones within
a Region, meaning your data is highly
durable with less chance of data loss.
• DynamoDB is automatically replicate
d across multiple Availability Zones,
providing high availability and data
durability.
• Amazon S3 provides 11 nines of durabilit
y. Many database services, such as Amazon
