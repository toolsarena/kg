---
title: "Scheduled scaling"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 588
---

# Scheduled scaling

Scheduled scaling provisions or removes resources based on the calendar or time of day. It is
frequently used for workloads that have predictable demand, such as peak utilization during
weekday business hours or sales events. Both Amazon EC2 Auto Scaling and Application Auto
Scaling support scheduled scaling. KEDA's cron scaler supports scheduled scaling of Kubernetes
pods.
