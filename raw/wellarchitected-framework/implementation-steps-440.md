---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 847
---

# Implementation steps

• Implement notifications on spend: Using your defined organization policies, create AWS
Budgets to notify you when spending is outside of your policies. Configure multiple cost budgets,
one for each account, which notify you about overall account spending. Configure additional cost
budgets within each account for smaller units within the account. These units vary depending
on your account structure. Some common examples are AWS Regions, workloads (using tags),
or AWS services. Configure an email distribution list as the recipient for notifications, and not an
individual's email account. You can configure an actual budget for when an amount is exceeded,
or use a forecasted budget for notifying on forecasted usage. You can also preconfigure AWS
Budget Actions that can enforce specific IAM or SCP policies, or stop target Amazon EC2 or
Amazon RDS instances. Budget Actions can be started automatically or require workflow
approval.
• Implement notifications on anomalous spend: Use AWS Cost Anomaly Detection to reduce your
surprise costs in your organization and analyze root cause of potential anomalous spend. Once
you create cost monitor to identify unusual spend at your specified granularity and configure
notifications in AWS Cost Anomaly Detection, it sends you alert when unusual spend is detected.
This will allow you to analyze root cause behind the anomaly and understand the impact on your
cost. Use AWS Cost Categories while configuring AWS Cost Anomaly Detection to identify which
project team or business unit team can analyze the root cause of the unexpected cost and take
timely necessary actions.
