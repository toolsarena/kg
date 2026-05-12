---
title: "Figure 24: Multi-AZ architecture"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 694
---

# Figure 24: Multi-AZ architecture

In addition to this HA architecture, you need to add backups of all data required to run your
workload. This is especially important for data that is constrained to a single zone such as
Amazon EBS volumes or Amazon Redshift clusters. If an AZ fails, you will need to restore this
data to another AZ. Where possible, you should also copy data backups to another AWS Region
as an additional layer of protection.
An less common alternative approach to single Region, multi-AZ DR is illustrated in the blog
post, Building highly resilient applications using Amazon Application Recovery Controller, Part
1: Single-Region stack. Here, the strategy is to maintain as much isolation between the AZs as
possible, like how Regions operate. Using this alternative strategy, you can choose an active/
active or active/passive approach.
