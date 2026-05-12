---
title: "OPS04-BP04 Implement dependency telemetry"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 143
---

# OPS04-BP04 Implement dependency telemetry

Dependency telemetry is essential for monitoring the health and performance of the external
services and components your workload relies on. It provides valuable insights into reachability,
timeouts, and other critical events related to dependencies such as DNS, databases, or third-
party APIs. When you instrument your application to emit metrics, logs, and traces about these
dependencies, you gain a clearer understanding of potential bottlenecks, performance issues, or
failures that might impact your workload.
Desired outcome: Ensure that the dependencies your workload relies on are performing as
expected, allowing you to proactively address issues and ensure optimal workload performance.
