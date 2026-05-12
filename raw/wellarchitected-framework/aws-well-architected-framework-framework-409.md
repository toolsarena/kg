---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 540
---

# AWS Well-Architected Framework Framework

long time is often not acceptable. Also, some use cases may require complete auditing entries to
fulfill compliance requirements.
5. A primary instance of a relational database may be unavailable: Amazon Relational Database
Service, like almost all relational databases, can only have one primary writer instance. This
creates a single point of failure for write workloads and makes scaling more difficult. This can
partially be mitigated by using a Multi-AZ configuration for high availability or Amazon Aurora
Serverless for better scaling. For very high availability requirements, it can make sense to not
rely on the primary writer at all. For queries that only read, read replicas can be used, which
provide redundancy and the ability to scale out, not just up. Writes can be buffered, for example
in an Amazon Simple Queue Service queue, so that write requests from customers can still be
accepted even if the primary is temporarily unavailable.
