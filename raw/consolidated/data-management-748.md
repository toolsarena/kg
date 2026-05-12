---
title: "Data management 748"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 753
---

# Data management 748

| Configuration option | Examples |
| --- | --- |
| Policies to manage the lifecycle of your
datasets | • You can use Amazon S3 Lifecycle to
manage your objects throughout their
lifecycle. If your access patterns are
unknown, changing, or unpredictable,
you can use Amazon S3 Intelligent-
Tiering, which monitors access patterns
and automatically moves objects that
have not been accessed to lower-cost
access tiers. You can leverage Amazon S3
Storage Lens metrics to identify optimizat
ion opportunities and gaps in lifecycle
management.
• Amazon EFS lifecycle managemen
t automatically manages file storage for
your file systems. |
| Connection management and pooling | • Amazon RDS Proxy can be used with
Amazon RDS and Aurora to manage
connections to the database.
• Serverless databases such as DynamoDB
do not have connections associated
with them, but consider the provisioned
capacity and automatic scaling policies to
deal with spikes in load. |


# Data management

The optimal data management solution for a particular system varies based on the kind of data
type (block, file, or object), access patterns (random or sequential), required throughput, frequency