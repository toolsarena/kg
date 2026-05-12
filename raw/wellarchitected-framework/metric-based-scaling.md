---
title: "Metric-based scaling"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 587
---

# Metric-based scaling

Metric-based scaling provisions resources based on the value of one or more scaling metrics. A
scaling metric is one that corresponds to your workload's demand. A good way to determine
appropriate scaling metrics is to perform load testing in a non-production environment. During
your load tests, keep the number of scalable resources fixed, and slowly increase demand (for
example, throughput, concurrency, or simulated users). Then look for metrics that increase (or
decrease) as demand grows, and conversely decrease (or increase) as demand falls. Typical scaling
metrics include CPU utilization, work queue depth (such as an Amazon SQS queue), number of
active users, and network throughput.
