---
title: "Amazon RDS and Aurora to manage"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 753
---

# Amazon RDS and Aurora to manage

connections to the database.
• Serverless databases such as DynamoDB
do not have connections associated
with them, but consider the provisioned
capacity and automatic scaling policies to
deal with spikes in load.
• Perform experiments and benchmarking in non-production environment to identify which
configuration option can address your workload requirements.
• Once you have experimented, plan your migration and validate your performance metrics.
• Use AWS monitoring (like Amazon CloudWatch) and optimization (like Amazon S3 Storage Lens)
tools to continuously optimize your data store using real-world usage pattern.
