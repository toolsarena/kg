---
title: "Failure management"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 42
---

# Failure management

In any system of reasonable complexity, it is expected that failures will occur. Reliability requires
that your workload be aware of failures as they occur and take action to avoid impact on
availability. Workloads must be able to both withstand failures and automatically repair issues.
With AWS, you can take advantage of automation to react to monitoring data. For example, when a
particular metric crosses a threshold, you can initiate an automated action to remedy the problem.
Also, rather than trying to diagnose and fix a failed resource that is part of your production
environment, you can replace it with a new one and carry out the analysis on the failed resource
out of band. Since the cloud allows you to stand up temporary versions of a whole system at low
cost, you can use automated testing to verify full recovery processes.
The following questions focus on these considerations for reliability.
REL 9: How do you back up data?
Back up data, applications, and configuration to meet your requirements for recovery time
objectives (RTO) and recovery point objectives (RPO).
