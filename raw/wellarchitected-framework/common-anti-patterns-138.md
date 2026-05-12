---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 563
---

# Common anti-patterns:

• You don't collect relevant logs or metrics from the compute instances your workloads run on or
the cloud services they use.
• You overlook the collection of logs and metrics related to your business key performance
indicators (KPIs).
• You analyze workload-related telemetry in isolation without aggregation and correlation.
• You allow metrics and logs to expire too quickly, which hinders trend analysis and recurring issue
identification.
Benefits of establishing these best practices: You can detect more anomalies and correlate events
and metrics between different components of your workload. You can create insights from your
workload components based on information contained in logs that frequently aren't available in
metrics alone. You can determine causes of failure more quickly by querying your logs at scale.
Level of risk exposed if these best practices are not established: High
