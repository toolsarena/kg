---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 685
---

# Implementation guidance

A DR strategy relies on the ability to stand up your workload in a recovery site if your primary
location becomes unable to run the workload. The most common recovery objectives are RTO and
RPO, as discussed in REL13-BP01 Define recovery objectives for downtime and data loss.
A DR strategy across multiple Availability Zones (AZs) within a single AWS Region, can provide
mitigation against disaster events like fires, floods, and major power outages. If it is a requirement
to implement protection against an unlikely event that prevents your workload from being able to
run in a given AWS Region, you can use a DR strategy that uses multiple Regions.
When architecting a DR strategy across multiple Regions, you should choose one of the following
strategies. They are listed in increasing order of cost and complexity, and decreasing order of
RTO and RPO. Recovery Region refers to an AWS Region other than the primary one used for your
workload.
