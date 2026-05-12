---
title: "Policy statement"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 833
---

# Policy statement

1. Select us-east-1or multiple us-east regions based on your workload’s environment and business
requirement (development, user acceptance testing, pre-production, or production).
2. Schedule Amazon EC2 and Amazon RDS instances to run between six in the morning and eight
at night (Eastern Standard Time (EST)).
3. Stop all unused Amazon EC2 instances after eight hours and unused Amazon RDS instances
after 24 hours of inactivity.
4. Terminate all unused Amazon EC2 instances after 24 hours of inactivity in non-production
environments. Remind Amazon EC2 instance owner (based on tags) to review their stopped
Amazon EC2 instances in production and inform them that their Amazon EC2 instances will be
terminated within 72 hours if they are not in use.
5. Use generic instance family and size such as m5.large and then resize the instance based on CPU
and memory utilization using AWS Compute Optimizer.
6. Prioritize using auto scaling to dynamically adjust the number of running instances based on
traffic.
7. Use spot instances for non-critical workloads.
8. Review capacity requirements to commit saving plans or reserved instances for predictable
workloads and inform Cloud Financial Management Team.
9. Use Amazon S3 lifecycle policies to move infrequently accessed data to cheaper storage tiers. If
no retention policy defined, use Amazon S3 Intelligent Tiering to move objects to archived tier
automatically.
10.Monitor resource utilization and set alarms to trigger scaling events using Amazon CloudWatch.
11.For each AWS account, use AWS Budgets to set cost and usage budgets for your account based
on cost center and business units.
12.Using AWS Budgets to set cost and usage budgets for your account can help you stay on top of
your spending and avoid unexpected bills, allowing you to better control your costs.
