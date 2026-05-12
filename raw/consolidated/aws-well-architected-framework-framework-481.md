---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 629
---

# AWS Well-Architected Framework Framework

Desired outcome: A cell-based architecture uses multiple isolated instances of a workload, where
each instance is known as a cell. Each cell is independent, does not share state with other cells, and
handles a subset of the overall workload requests. This reduces the potential impact of a failure,
such as a bad software update, to an individual cell and the requests it is processing. If a workload
uses 10 cells to service 100 requests, when a failure occurs, 90% of the overall requests would be
unaffected by the failure.
