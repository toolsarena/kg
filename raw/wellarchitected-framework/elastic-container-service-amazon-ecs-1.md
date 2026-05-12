---
title: "Elastic Container Service (Amazon ECS)"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 735
---

# Elastic Container Service (Amazon ECS)

services.
Kubernetes Cluster Autoscaler/Karpenter To automatically scale Kubernetes clusters.
• Scaling is often discussed related to compute services like Amazon EC2 Instances or AWS Lambda
functions. Be sure to also consider the configuration of non-compute services like AWS Glue to
match the demand.
• Verify that the metrics for scaling match the characteristics of the workload being deployed. If
you are deploying a video transcoding application, 100% CPU utilization is expected and should
not be your primary metric. Use the depth of the transcoding job queue instead. You can use a
customized metric for your scaling policy if required. To choose the right metrics, consider the
following guidance for Amazon EC2:
• The metric should be a valid utilization metric and describe how busy an instance is.
