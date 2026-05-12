---
title: "DocumentDB all support adding read"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 751
---

# DocumentDB all support adding read

replicas to offload the read portions of the
workload.
• Serverless databases such as DynamoDB
will scale automatically. Ensure that you
have enough read capacity units (RCU)
provisioned to handle the workload.
Scaling writes (like partition key sharding or • For relational databases, you can increase
introducing a queue) the size of the instance to accommoda
te an increased workload or increase the
provisioned IOPs to allow for an increased
throughput to the underlying storage.
