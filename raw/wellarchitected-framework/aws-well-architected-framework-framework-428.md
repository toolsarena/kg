---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 561
---

# AWS Well-Architected Framework Framework

to log workload specific data. Collect metrics for CPU, network I/O, and disk I/O averages from
services such as Amazon ECS, Amazon EKS, Amazon EC2, Elastic Load Balancing, AWS Auto
Scaling, and Amazon EMR. See AWS Services That Publish CloudWatch Metrics for a list of AWS
services that publish metrics to CloudWatch.
2. Review all default metrics and explore any data collection gaps. Every service generates
default metrics. Collecting default metrics allows you to better understand the dependencies
between workload components, and how component reliability and performance affect the
workload. You can also create and publish your own metrics to CloudWatch using the AWS CLI or
an API.
3. Evaluate all the metrics to decide which ones to alert on for each AWS service in your
workload. You may choose to select a subset of metrics that have a major impact on workload
reliability. Focusing on critical metrics and threshold allows you to refine the number of alerts
and can help minimize false-positives.
4. Define alerts and the recovery process for your workload after the alert is invoked. Defining
alerts allows you to quickly notify, escalate, and follow steps necessary to recover from an
incident and meet your prescribed Recovery Time Objective (RTO). You can use Amazon
CloudWatch Alarms to invoke automated workflows and initiate recovery procedures based on
defined thresholds.
5. Explore use of synthetic transactions to collect relevant data about workloads state.
Synthetic monitoring follows the same routes and perform the same actions as a customer,
which makes it possible for you to continually verify your customer experience even when you
don't have any customer traffic on your workloads. By using synthetic transactions, you can
discover issues before your customers do.
