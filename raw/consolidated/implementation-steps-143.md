---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 699
---

# Implementation steps

1. Engineer your workloads for recovery. Regularly test your recovery paths. Recovery-oriented
computing identifies the characteristics in systems that enhance recovery: isolation and
redundancy, system-wide ability to roll back changes, ability to monitor and determine health,
ability to provide diagnostics, automated recovery, modular design, and ability to restart.
Exercise the recovery path to verify that you can accomplish the recovery in the specified time
to the specified state. Use your runbooks during this recovery to document problems and find
solutions for them before the next test.
2. For Amazon EC2-based workloads, use AWS Elastic Disaster Recovery to implement and launch
drill instances for your DR strategy. AWS Elastic Disaster Recovery provides the ability to
efficiently run drills, which helps you prepare for a failover event. You can also frequently launch
of your instances using Elastic Disaster Recovery for test and drill purposes without redirecting
the traffic.
