---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 730
---

# Implementation guidance

Cloud workloads can generate large volumes of data such as metrics, logs, and events. In the
AWS Cloud, collecting metrics is a crucial step to improve security, cost efficiency, performance,
and sustainability. AWS provides a wide range of performance-related metrics using monitoring
services such as Amazon CloudWatch to provide you with valuable insights. Metrics such as CPU
utilization, memory utilization, disk I/O, and network inbound and outbound can provide insight
into utilization levels or performance bottlenecks. Use these metrics as part of a data-driven
approach to actively tune and optimize your workload's resources. In an ideal case, you should
collect all metrics related to your compute resources in a single platform with retention policies
implemented to support cost and operational goals.
