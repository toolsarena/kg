---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 729
---

# Common anti-patterns:

• You only use manual log file searching for metrics.
• You only use the default metrics recorded by your monitoring software.
• You only review metrics when there is an issue.
Benefits of establishing this best practice: Collecting performance-related metrics will help you
align application performance with business requirements to ensure that you are meeting your
workload needs. It can also help you continually improve the resource performance and utilization
in your workload.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• Overlooking trace data, relying solely on logs and metrics.
• Not correlating trace data with associated logs.
• Ignoring the metrics derived from traces, such as latency and fault rates.