---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 886
---

# Implementation guidance

Perform cost modeling for your workload and each of its components to understand the balance
between resources, and find the correct size for each resource in the workload, given a specific level
of performance. Understanding cost considerations can inform your organizational business case
and decision-making process when evaluating the value realization outcomes for planned workload
deployment.
Perform benchmark activities for the workload under different predicted loads and compare the
costs. The modeling effort should reflect potential benefit; for example, time spent is proportional
to component cost or predicted saving. For best practices, refer to the Review section of the
Performance Efficiency Pillar of the AWS Well-Architected Framework.
As an example, to create cost modeling for a workload consisting of compute resources, AWS
Compute Optimizer can assist with cost modeling for running workloads. It provides right-sizing
recommendations for compute resources based on historical usage. Make sure CloudWatch
Agents are deployed to the Amazon EC2 instances to collect memory metrics which help you with
more accurate recommendations within AWS Compute Optimizer. This is the ideal data source
for compute resources because it is a free service that uses machine learning to make multiple
recommendations depending on levels of risk.
There are multiple services you can use with custom logs as data sources for rightsizing operations
for other services and workload components, such as AWS Trusted Advisor, Amazon CloudWatch
and Amazon CloudWatch Logs. AWS Trusted Advisor checks resources and flags resources with low
utilization which can help you rightsize your resources and create cost modeling.
