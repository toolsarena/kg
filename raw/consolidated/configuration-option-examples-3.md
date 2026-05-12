---
title: "Configuration option Examples"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 752
---

# Configuration option Examples

• You can also introduce a queue in front of
your database rather than writing directly
to the database. This pattern allows you to
decouple the ingestion from the database
and control the flow-rate so the database
does not get overwhelmed.
• Batching your write requests rather than
creating many short-lived transactions can
help improve throughput in high-write
volume relational databases.
• Serverless databases like DynamoDB can
scale the write throughput automatically or
by adjusting the provisioned write capacity
units (WCU) depending on the capacity
mode.
• You can still run into issues with hot
partitions when you reach the throughpu
t limits for a given partition key. This can
be mitigated by choosing a more evenly
distributed partition key or by write-sha
rding the partition key.


# Configuration option Examples

Policies to manage the lifecycle of your • You can use Amazon S3 Lifecycle to
datasets manage your objects throughout their
lifecycle. If your access patterns are
unknown, changing, or unpredictable,
you can use Amazon S3 Intelligent-