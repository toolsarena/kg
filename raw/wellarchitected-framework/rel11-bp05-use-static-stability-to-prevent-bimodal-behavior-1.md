---
title: "REL11-BP05 Use static stability to prevent bimodal behavior"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 647
---

# REL11-BP05 Use static stability to prevent bimodal behavior

Workloads should be statically stable and only operate in a single normal mode. Bimodal behavior
is when your workload exhibits different behavior under normal and failure modes.
For example, you might try and recover from an Availability Zone failure by launching new
instances in a different Availability Zone. This can result in a bimodal response during a failure
mode. You should instead build workloads that are statically stable and operate within only one
mode. In this example, those instances should have been provisioned in the second Availability
Zone before the failure. This static stability design verifies that the workload only operates in a
single mode.
Desired outcome: Workloads do not exhibit bimodal behavior during normal and failure modes.
