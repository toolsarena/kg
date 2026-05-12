---
title: "Data management 743"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 748
---

# Data management 743

| Question | Things to consider |
| --- | --- |
| Is there a desire to move away from
commercial database engines or licensing
costs? | • Consider open-source engines such as
PostgreSQL and MySQL on Amazon RDS or
Aurora.
• Leverage AWS Database Migration Service
and AWS Schema Conversion Tool to
perform migrations from commercial
database engines to open-source |
| What is the operational expectation for the
database? Is moving to managed services a
primary concern? | • Leveraging Amazon RDS instead of
Amazon EC2, and DynamoDB or Amazon
DocumentDB instead of self-hosting a
NoSQL database can reduce operational
overhead. |
| How is the database currently accessed? Is it
only application access, or are there business
intelligence (BI) users and other connected
off-the-shelf applications? | • If you have dependencies on external
tooling then you may have to maintain
compatibility with the databases they
support. Amazon RDS is fully compatible
with the difference engine versions that it
supports including Microsoft SQL Server,
Oracle, MySQL, and PostgreSQL. |
