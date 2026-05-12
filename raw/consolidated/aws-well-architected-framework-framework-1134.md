---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 502
---

# AWS Well-Architected Framework Framework

• Note that the initial VPC CIDR block allocated to your VPC cannot be changed or deleted, but
you can add additional non-overlapping CIDR blocks to the VPC. Subnet IPv4 CIDRs cannot be
changed, however IPv6 CIDRs can.
• The largest possible VPC CIDR block is a /16, and the smallest is a /28.
• Consider other connected networks (VPC, on-premises, or other cloud providers) and ensure non-
overlapping IP address space. For more information, see REL02-BP05 Enforce non-overlapping
private IP address ranges in all private address spaces where they are connected.
Desired outcome: A scalable IP subnet can help you accomodate for future growth and avoid
unnecessary waste.
