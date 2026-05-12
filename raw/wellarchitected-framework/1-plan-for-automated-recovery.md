---
title: "1. Plan for automated recovery"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 704
---

# 1. Plan for automated recovery

a. Conduct a thorough review of your workload architecture, components, and dependencies to
identify and plan automated recovery mechanisms. Categorize your workload's dependencies
into hard and soft dependencies. Hard dependencies are those that the workload cannot
operate without and for which no substitute can be provided. Soft dependencies are those
that the workload ordinarily uses but are replaceable with temporary substitute systems or
processes or can be handled by graceful degradation.
b. Establish processes to identify and recover missing or corrupted data.
c. Define steps to confirm a recovered steady state after recovery actions have been completed.
d. Consider any actions required to make the recovered system ready for full service, such as
pre-warming and populating caches.
