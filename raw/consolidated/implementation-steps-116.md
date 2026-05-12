---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 576
---

# Implementation steps

1. Schedule and conduct regular reviews of the workload dashboards. You may have different
cadences for the depth at which you inspect.
2. Inspect for trends in the metrics. Compare the metric values to historic values to see if there
are trends that may indicate that something that needs investigation. Examples of this include
increased latency, decreased primary business function, and increased failure responses.
3. Inspect for outliers and anomalies in your metrics, which can be masked by averages or medians.
Look at the highest and lowest values during the time frame, and investigate the causes of
observations that are far outside of normal bounds. As you continue to remove these causes,
you can tighten your expected metric bounds in response to the improved consistency of your
workload performance.
