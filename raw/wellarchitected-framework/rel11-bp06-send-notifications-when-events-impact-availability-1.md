---
title: "REL11-BP06 Send notifications when events impact availability"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 651
---

# REL11-BP06 Send notifications when events impact availability

Notifications are sent upon the detection of thresholds breached, even if the event causing the
issue was automatically resolved.
Automated healing allows your workload to be reliable. However, it can also obscure underlying
problems that need to be addressed. Implement appropriate monitoring and events so that you
can detect patterns of problems, including those addressed by auto healing, so that you can
resolve root cause issues.
Resilient systems are designed so that degradation events are immediately communicated to
the appropriate teams. These notifications should be sent through one or many communication
channels.
Desired outcome: Alerts are immediately sent to operations teams when thresholds are breached,
such as error rates, latency, or other critical key performance indicator (KPI) metrics, so that these
issues are resolved as soon as possible and user impact is avoided or minimized.
