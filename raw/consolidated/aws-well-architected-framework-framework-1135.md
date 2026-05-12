---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 503
---

# AWS Well-Architected Framework Framework

• Determine if you are going to deploy multi-VPC connectivity.
• What Is a Transit Gateway?
• Single Region Multi-VPC Connectivity
• Determine if you need segregated networking for regulatory requirements.
• Make VPCs with appropriately-sized CIDR blocks to accommodate your current and future
needs.
• If you have unknown growth projections, you may wish to err on the side of larger CIDR
blocks to reduce the potential for future reconfiguration
• Consider using IPv6 addressing for subnets as part of a dual-stack VPC. IPv6 is well suited
to being used in private subnets containing fleets of ephemeral instances or containers that
would otherwise require large numbers of IPv4 addresses.
