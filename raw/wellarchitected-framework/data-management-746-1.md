---
title: "Data management 746"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 751
---

# Data management 746

| Configuration option | Examples |
| --- | --- |
| Offloading reads (like read replicas and
caching) | • For DynamoDB tables, you can offload
reads using DAX for caching.
• You can create an Amazon ElastiCac
he (Redis OSS) cluster and configure
your application to read from the cache
first, falling back to the database if the
requested item is not present.
• Relational databases such as Amazon
RDS and Aurora, and provisioned NoSQL
databases such as Neptune and Amazon
DocumentDB all support adding read
replicas to offload the read portions of the
workload.
• Serverless databases such as DynamoDB
will scale automatically. Ensure that you
have enough read capacity units (RCU)
provisioned to handle the workload. |
| Scaling writes (like partition key sharding or
introducing a queue) | • For relational databases, you can increase
the size of the instance to accommoda
te an increased workload or increase the
provisioned IOPs to allow for an increased
throughput to the underlying storage. |
