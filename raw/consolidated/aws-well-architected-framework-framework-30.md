---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 43
---

# AWS Well-Architected Framework Framework

REL 10: How do you use fault isolation to protect your workload?
Fault isolation limits the impact of a component or system failure to a defined boundary. With
proper isolation, components outside of the boundary are unaffected by the failure. Running
your workload across multiple fault isolation boundaries can make it more resilient to failure.
REL 11: How do you design your workload to withstand component failures?
Workloads with a requirement for high availability and low mean time to recovery (MTTR) must
be architected for resiliency.
REL 12: How do you test reliability?
After you have designed your workload to be resilient to the stresses of production, testing is
the only way to verify that it will operate as designed, and deliver the resiliency you expect.
REL 13: How do you plan for disaster recovery (DR)?
Having backups and redundant workload components in place is the start of your DR strategy.
RTO and RPO are your objectives for restoration of your workload. Set these based on business
needs. Implement a strategy to meet these objectives, considering locations and function of
workload resources and data. The probability of disruption and cost of recovery are also key
factors that help to inform the business value of providing disaster recovery for a workload.
Regularly back up your data and test your backup files to verify that you can recover from both
logical and physical errors. A key to managing failure is the frequent and automated testing of
workloads to cause failure, and then observe how they recover. Do this on a regular schedule
and verify that such testing is also initiated after significant workload changes. Actively track
KPIs, and also the recovery time objective (RTO) and recovery point objective (RPO), to assess a
workload's resiliency (especially under failure-testing scenarios). Tracking KPIs will help you identify
and mitigate single points of failure. The objective is to thoroughly test your workload-recovery
processes so that you are confident that you can recover all your data and continue to serve your
