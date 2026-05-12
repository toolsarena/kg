---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 846
---

# Implementation guidance

A common first step in implementing cost controls is to set up notifications when cost or usage
events occur outside of policies. You can act quickly and verify if corrective action is required
without restricting or negatively impacting workloads or new activity. After you know the workload
and environment limits, you can enforce governance. AWS Budgets allows you to set notifications
and define monthly budgets for your AWS costs, usage, and commitment discounts (Savings Plans
and Reserved Instances). You can create budgets at an aggregate cost level (for example, all costs),
or at a more granular level where you include only specific dimensions such as linked accounts,
services, tags, or Availability Zones.
Once you set up your budget limits with AWS Budgets, use AWS Cost Anomaly Detection to reduce
your unexpected cost. AWS Cost Anomaly Detection is a cost management service that uses
machine learning to continually monitor your cost and usage to detect unusual spends. It helps
you identify anomalous spend and root causes, so you can quickly take action. First, create a cost
monitor in AWS Cost Anomaly Detection, then choose your alerting preference by setting up a
dollar threshold (such as an alert on anomalies with impact greater than $1,000). Once you receive
alerts, you can analyze the root cause behind the anomaly and impact on your costs. You can also
monitor and perform your own anomaly analysis in AWS Cost Explorer.
Enforce governance policies in AWS through AWS Identity and Access Management and AWS
Organizations Service Control Policies (SCP). IAM allows you to securely manage access to AWS
services and resources. Using IAM, you can control who can create or manage AWS resources,
