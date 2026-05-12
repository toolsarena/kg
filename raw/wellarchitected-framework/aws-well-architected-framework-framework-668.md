---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 876
---

# AWS Well-Architected Framework Framework

for that service increases, transitioning to EMR on EC2 could reduce costs for that component of
the workload.
AWS Cost Explorer and the AWS Cost and Usage Reports (CUR) can analyze the cost of a proof
of concept (PoC) or running environment. You can also use AWS Pricing Calculator to estimate
workload costs.
Write a workflow to be followed by technical teams to review their workloads. Keep this workflow
simple, but also cover all the necessary steps to make sure the teams understand each component
of the workload and its pricing. Your organization can then follow and customize this workflow
based on the specific needs of each team.
1. List each service in use for your workload: This is a good starting point. Identify all of the
services currently in use and where costs are originate from.
2. Understand how pricing works for those services: Understand the pricing model of each
service. Different AWS services have different pricing models based on factors like usage volume,
data transfer, and feature-specific pricing.
3. Focus on the services that have unexpected workload costs and that do not align with your
expected usage and business outcome: Identify outliers or services where the cost is not
proportional to the value or usage by using AWS Cost Explorer or AWS Cost and Usage Reports.
It's important to correlate costs with business outcomes to prioritize optimization efforts.
4. AWS Cost Explorer, CloudWatch Logs, VPC Flow Logs, and Amazon S3 Storage Lens to
understand the root cause of those high costs: These tools are instrumental in the diagnosis of
high costs. Each service offers a different lens to view and analyze usage and costs. For instance,
Cost Explorer helps determine overall cost trends, CloudWatch Logs provides operational
insights, VPC Flow Logs displays IP traffic, and Amazon S3 Storage Lens is useful for storage
analytics.
5. Use AWS Budgets to set budgets for certain amounts for services or accounts: Setting budgets
is a proactive way to manage costs. Use AWS Budgets to set custom budget thresholds and
receive alerts when costs exceed those thresholds.
6. Configure Amazon CloudWatch alarms to send billing and usage alerts: Set up monitoring
and alerts for cost and usage metrics. CloudWatch alarms can notify you when certain
thresholds are breached, which improves intervention response time.
Facilitate notable enhancement and financial savings over time through strategic review of all
workload components and irrespective of their present attributes. The effort invested in this review
