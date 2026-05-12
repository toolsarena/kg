---
title: "Data management 740"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 745
---

# Data management 740

| Type | AWS Services | Key characteristics |
| --- | --- | --- |
| Wide column | Amazon Keyspaces (for
Apache Cassandra) | Uses tables, rows, and
columns, but unlike a
relational database, the
names and format of the
columns can vary from
row to row in the same
table. You typically see a
wide column store in high
scale industrial apps for
equipment maintenance,
fleet management, and route
optimization. |
| Ledger | Amazon Quantum Ledger
Database (Amazon QLDB) | Provides a centralized and
trusted authority to maintain
a scalable, immutable, and
cryptographically verifiabl
e record of transactions for
every application. We see
ledger databases used for
systems of record, supply
chain, registrations, and even
banking transactions. |

| Question | Things to consider |
| --- | --- |
| How is the data structured? | • If the data is unstructured, consider
an object-store such as Amazon S3 or
a NoSQL database such as Amazon
DocumentDB |
