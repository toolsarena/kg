---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 670
---

# AWS Well-Architected Framework Framework

Chaos engineering and continuous resilience flywheel, using the scientific method by Adrian
Hornsby.
a. Define steady state as some measurable output of a workload that indicates normal behavior.
Your workload exhibits steady state if it is operating reliably and as expected. Therefore,
validate that your workload is healthy before defining steady state. Steady state does not
necessarily mean no impact to the workload when a fault occurs, as a certain percentage
in faults could be within acceptable limits. The steady state is your baseline that you will
observe during the experiment, which will highlight anomalies if your hypothesis defined in
the next step does not turn out as expected.
For example, a steady state of a payments system can be defined as the processing of 300
TPS with a success rate of 99% and round-trip time of 500 ms.
b. Form a hypothesis about how the workload will react to the fault.
