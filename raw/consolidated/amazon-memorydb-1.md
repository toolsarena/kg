---
title: "Amazon MemoryDB"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 746
---

# Amazon MemoryDB

What level of referential integrity is required? • For foreign key constraints, relational
databases such as Amazon RDS and Aurora
can provide this level of integrity.
• Typically, within a NoSQL data-model, you
would de-normalize your data into a single
document or collection of documents to
be retrieved in a single request rather than
joining across documents or tables.
Is ACID (atomicity, consistency, isolation, • If the ACID properties associated with
durability) compliance required? relational databases are required, consider
a relational database such as Amazon RDS
and Aurora.
• If strong consistency is required for NoSQL
database, you can use strongly consistent
reads with DynamoDB.
How will the storage requirements change • Serverless databases such as DynamoDB
over time? How does this impact scalability? and Amazon Quantum Ledger Database
(Amazon QLDB) will scale dynamically.
• Relational databases have upper bounds
on provisioned storage, and often must be
horizontally partitioned using mechanism
s such as sharding once they reach these
limits.


# Amazon MemoryDB for Redis require real-time access to

data, lowest latency and
highest throughput. You may
use in-memory databases for
application caching, session
management, gaming
leaderboards, low latency

# Amazon MemoryDB for Redis require real-time access to

data, lowest latency and
highest throughput. You may
use in-memory databases for
application caching, session
management, gaming
leaderboards, low latency