---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 870
---

# Implementation guidance

Use automation to reduce or remove the associated costs of the decommissioning process.
Designing your workload to perform automated decommissioning will reduce the overall workload
costs during its lifetime. You can use Amazon EC2 Auto Scaling or Application Auto Scaling to
perform the decommissioning process. You can also implement custom code using the API or SDK
to decommission workload resources automatically.
Modern applications are built serverless-first, a strategy that prioritizes the adoption of serverless
services. AWS developed serverless services for all three layers of your stack: compute, integration,
and data stores. Using serverless architecture will allow you to save costs during low-traffic periods
with scaling up and down automatically.
