---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 633
---

# Common anti-patterns:

• No alarms have been configured, so outages occur without notification.
• Alarms exist, but at thresholds that don't provide adequate time to react.
• Metrics are not collected often enough to meet the recovery time objective (RTO).
• Only the customer facing interfaces of the workload are actively monitored.
• Only collecting technical metrics, no business function metrics.
• No metrics measuring the user experience of the workload.
• Too many monitors are created.
Benefits of establishing this best practice: Having appropriate monitoring at all layers allows you
to reduce recovery time by reducing time to detection.
Level of risk exposed if this best practice is not established: High
