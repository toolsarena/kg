---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 545
---

# Implementation guidance

Control and limit retry calls. Use exponential backoff to retry after progressively longer intervals.
Introduce jitter to randomize retry intervals and limit the maximum number of retries.
Some AWS SDKs implement retries and exponential backoff by default. Use these built-in AWS
implementations where applicable in your workload. Implement similar logic in your workload
