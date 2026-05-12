---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 717
---

# Implementation guidance

Use benchmarking with synthetic tests to assess how your workload’s components perform.
Benchmarking is generally quicker to set up than load testing and is used to evaluate the
technology for a particular component. Benchmarking is often used at the start of a new project,
when you lack a full solution to load test.
You can either build your own custom benchmark tests or use an industry standard test, such
as TPC-DS, to benchmark your workloads. Industry benchmarks are helpful when comparing
environments. Custom benchmarks are useful for targeting specific types of operations that you
expect to make in your architecture.
When benchmarking, it is important to pre-warm your test environment to get valid results. Run
the same benchmark multiple times to verify that you’ve captured any variance over time.
