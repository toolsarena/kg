---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 654
---

# Implementation guidance

Application designs have to account for a diverse set of requirements that are derived from
business, operational, and financial objectives. Within the operational requirements, workloads
need to have specific resilience metric targets so they can be properly monitored and supported.
Resilience metrics should not be set or derived after deploying the workload. They should be
defined during the design phase and help guide various decisions and tradeoffs.
• Every workload should have its own set of resilience metrics. Those metrics may be different
from other business applications.
• Reducing dependencies can have a positive impact on availability. Each workload should consider
its dependencies and their SLAs. In general, select dependencies with availability goals equal to
or greater than the goals of your workload.
• Consider loosely coupled designs so your workload can operate correctly despite dependency
impairment, where possible.
• Reduce control plane dependencies, especially during recovery or a degradation. Evaluate
designs that are statically stable for mission critical workloads. Use resource sparing to increase
the availability of those dependencies in a workload.
• Observability and instrumentation are critical for achieving SLAs by reducing Mean Time to
Detection (MTTD) and Mean Time to Repair (MTTR).
