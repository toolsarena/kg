---
title: "REL05-BP07 Implement emergency levers"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 556
---

# REL05-BP07 Implement emergency levers

Emergency levers are rapid processes that can mitigate availability impact on your workload.
Emergency levers work by disabling, throttling, or changing the behavior of components or
dependencies using known and tested mechanisms. This can alleviate workload impairments
caused by resource exhaustion due to unexpected increases in demand and reduce the impact of
failures in non-critical components within your workload.
Desired outcome: By implementing emergency levers, you can establish known-good processes
to maintain the availability of critical components in your workload. The workload should degrade
gracefully and continue to perform its business-critical functions during the activation of an
emergency lever. For more detail on graceful degradation, see REL05-BP01 Implement graceful
degradation to transform applicable hard dependencies into soft dependencies.
