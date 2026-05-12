---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 802
---

# Implementation guidance

Use alarms to trigger automated actions to remediate issues where possible. Escalate the alarm to
those able to respond if automated response is not possible. For example, you may have a system
that can predict expected key performance indicator (KPI) values and alarm when they breach
certain thresholds, or a tool that can automatically halt or roll back deployments if KPIs are outside
of expected values.
Implement processes that provide visibility into performance as your workload is running. Build
monitoring dashboards and establish baseline norms for performance expectations to determine if
the workload is performing optimally.
