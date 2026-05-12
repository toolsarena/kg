---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 730
---

# Implementation steps

• Identify which performance-related metrics are relevant to your workload. You should collect
metrics around resource utilization and the way your cloud workload is operating (like response
time and throughput).
• Amazon EC2 default metrics
• Amazon ECS default metrics
• Amazon EKS default metrics
• Lambda default metrics
• Amazon EC2 memory and disk metrics
• Choose and set up the right logging and monitoring solution for your workload.
• AWS native Observability
• AWS Distro for OpenTelemetry
• Amazon Managed Service for Prometheus
• Define the required filter and aggregation for the metrics based on your workload requirements.
• Quantify custom application metrics with Amazon CloudWatch Logs and metric filters
• Collect custom metrics with Amazon CloudWatch strategic tagging
• Configure data retention policies for your metrics to match your security and operational goals.
• Default data retention for CloudWatch metrics
• Default data retention for CloudWatch Logs
• If required, create alarms and notifications for your metrics to help you proactively respond to
performance-related issues.


# Implementation steps

• Choose an instance type to best fit your needs:

# Implementation steps

• Compute instances, containers, and functions provide mechanisms for elasticity, either in
combination with autoscaling or as a feature of the service. Here are some examples of
automatic scaling mechanisms:

# Implementation steps

• Identify which accelerated computing instances can address your requirements.
• For machine learning workloads, take advantage of purpose-built hardware that is specific to
your workload, such as AWS Trainium, AWS Inferentia, and Amazon EC2 DL1. AWS Inferentia