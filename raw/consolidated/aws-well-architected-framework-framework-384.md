---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 506
---

# AWS Well-Architected Framework Framework

Consider using a separate subnet for each transit gateway VPC attachment. For each subnet,
use a small CIDR (for example /28) so that you have more address space for compute resources.
Additionally, create one network ACL, and associate it with all of the subnets that are associated
with the hub. Keep the network ACL open in both the inbound and outbound directions.
Design and implement your routing tables such that routes are provided only between networks
that should communicate. Omit routes between networks that should not communicate with one
another (for example, between separate workloads that have no inter-dependencies).


# AWS Well-Architected Framework Framework

• APN Partner: partners that can help plan your networking
• AWS Marketplace for Network Infrastructure