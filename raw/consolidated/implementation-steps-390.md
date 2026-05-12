---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 668
---

# Implementation steps

1. Determine which faults to use for experiments.
Assess the design of your workload for resiliency. Such designs (created using the best practices
of the Well-Architected Framework) account for risks based on critical dependencies, past
events, known issues, and compliance requirements. List each element of the design intended to
maintain resilience and the faults it is designed to mitigate. For more information about creating
such lists, see the Operational Readiness Review whitepaper which guides you on how to create
a process to prevent reoccurrence of previous incidents. The Failure Modes and Effects Analysis
(FMEA) process provides you with a framework for performing a component-level analysis of
failures and how they impact your workload. FMEA is outlined in more detail by Adrian Cockcroft
in Failure Modes and Continuous Resilience.
2. Assign a priority to each fault.
