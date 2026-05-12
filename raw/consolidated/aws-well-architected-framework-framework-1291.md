---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 704
---

# AWS Well-Architected Framework Framework

workload. Develop automated processes that can recover your workloads and data from failures
without human intervention.
Develop your recovery automation using infrastructure as code (IaC) principles. This makes your
recovery environment consistent with the source environment and allows for version control of
your recovery processes. To orchestrate complex recovery workflows, consider solutions such as
AWS Systems Manager Automations or AWS Step Functions.
Automation of recovery processes provides significant benefits and can help you more easily
achieve your Recovery Time Objective (RTO) and Recovery Point Objective (RPO). However, they
can encounter unexpected situations that may cause them to fail or create new risks of their own
such as additional downtime and data loss. To mitigate this risk, provide the ability to quickly halt a
recovery automation in progress. Once halted, you can investigate and take corrective steps.
For supported workloads, consider solutions such as AWS Elastic Disaster Recovery (AWS DRS) to
provide automated failover. AWS DRS continually replicates your machines (including operating
system, system state configuration, databases, applications, and files) into a staging area in
your target AWS account and preferred Region. If an incident occurs, AWS DRS automates the
conversion of your replicated servers into fully-provisioned workloads in your recovery Region on
