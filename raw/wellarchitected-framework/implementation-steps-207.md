---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 890
---

# Implementation steps

• Increase your observability by configuring workload metrics: Capture key metrics for the
workload. These metrics provide an indication of the customer experience, such as workload
output, and align to the differences between resource types and sizes, such as CPU and memory
usage. For compute resource, analyze performance data to right size your Amazon EC2 instances.
Identify idle instances and ones that are underutilized. Key metrics to look for are CPU usage
and memory utilization (for example, 40% CPU utilization at 90% of the time as explained in
Rightsizing with AWS Compute Optimizer and Memory Utilization Enabled). Identify instances
with a maximum CPU usage and memory utilization of less than 40% over a four-week period.
These are the instances to right size to reduce costs. For storage resources such as Amazon
S3, you can use Amazon S3 Storage Lens, which allows you to see 28 metrics across various
categories at the bucket level, and 14 days of historical data in the dashboard by default. You can
filter your Amazon S3 Storage Lens dashboard by summary and cost optimization or events to
analyze specific metrics.
• View rightsizing recommendations: Use the rightsizing recommendations in AWS Compute
Optimizer and the Amazon EC2 rightsizing tool in the Cost Management console, or review
AWS Trusted Advisor right-sizing your resources to make adjustments on your workload. It is
important to use the right tools when right-sizing different resources and follow right-sizing
