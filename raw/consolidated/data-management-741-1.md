---
title: "Data management 741"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 746
---

# Data management 741

| Question | Things to consider |
| --- | --- |
|  | • For key-value data, consider DynamoDB,
Amazon ElastiCache (Redis OSS) or
Amazon MemoryDB |
| What level of referential integrity is required? | • For foreign key constraints, relational
databases such as Amazon RDS and Aurora
can provide this level of integrity.
• Typically, within a NoSQL data-model, you
would de-normalize your data into a single
document or collection of documents to
be retrieved in a single request rather than
joining across documents or tables. |
| Is ACID (atomicity, consistency, isolation,
durability) compliance required? | • If the ACID properties associated with
relational databases are required, consider
a relational database such as Amazon RDS
and Aurora.
• If strong consistency is required for NoSQL
database, you can use strongly consistent
reads with DynamoDB. |
| How will the storage requirements change
over time? How does this impact scalability? | • Serverless databases such as DynamoDB
and Amazon Quantum Ledger Database
(Amazon QLDB) will scale dynamically.
• Relational databases have upper bounds
on provisioned storage, and often must be
horizontally partitioned using mechanism
s such as sharding once they reach these
limits. |
