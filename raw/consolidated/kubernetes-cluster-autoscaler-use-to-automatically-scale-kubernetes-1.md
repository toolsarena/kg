---
title: "Kubernetes Cluster Autoscaler Use to automatically scale Kubernetes"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 938
---

# Kubernetes Cluster Autoscaler Use to automatically scale Kubernetes

clusters on AWS.
• Scaling is often discussed related to compute services like Amazon EC2 instances or AWS Lambda
functions. Consider the configuration of non-compute services like Amazon DynamoDB read and
write capacity units or Amazon Kinesis Data Streams shards to match the demand.
• Verify that the metrics for scaling up or down are validated against the type of workload being
deployed. If you are deploying a video transcoding application, 100% CPU utilization is expected
and should not be your primary metric. You can use a customized metric (such as memory
utilization) for your scaling policy if required. To choose the right metrics, consider the following
guidance for Amazon EC2:
• The metric should be a valid utilization metric and describe how busy an instance is.
• The metric value must increase or decrease proportionally to the number of instances in the
Auto Scaling group.
• Use dynamic scaling instead of manual scaling for your Auto Scaling group. We also recommend
that you use target tracking scaling policies in your dynamic scaling.
• Verify that workload deployments can handle both scale-out and scale-in events. Create test
scenarios for scale-in events to verify that the workload behaves as expected and does not affect
