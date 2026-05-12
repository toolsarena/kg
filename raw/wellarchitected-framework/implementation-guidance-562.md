---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 916
---

# Implementation guidance

Implementing a buffer or throttle is crucial in cloud computing in order to manage demand and
reduce the provisioned capacity required for your workload. For optimal performance, it's essential
to gauge the total demand, including peaks, the pace of change in requests, and the necessary
response time. When clients have the ability to resend their requests, it becomes practical to apply
throttling. Conversely, for clients lacking retry functionalities, the ideal approach is implementing
a buffer solution. Such buffers streamline the influx of requests and optimize the interaction of
applications with varied operational speeds.
