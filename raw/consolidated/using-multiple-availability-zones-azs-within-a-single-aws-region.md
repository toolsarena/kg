---
title: "Using multiple Availability Zones (AZs) within a single AWS Region"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 693
---

# Using multiple Availability Zones (AZs) within a single AWS Region

When using multiple AZs within a single Region, your DR implementation uses multiple
elements of the above strategies. First you must create a high-availability (HA) architecture,
using multiple AZs as shown in Figure 23. This architecture makes use of a multi-site active/
active approach, as the Amazon EC2 instances and the Elastic Load Balancer have resources
deployed in multiple AZs, actively handing requests. The architecture also demonstrates hot
