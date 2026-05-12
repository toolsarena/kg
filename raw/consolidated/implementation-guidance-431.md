---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 505
---

# Implementation guidance

Create a Network Services account if one does not exist. Place the hub in the organization's
Network Services account. This approach allows the hub to be centrally managed by network
engineers.
The hub of the hub-and-spoke model acts as a virtual router for traffic flowing between your
Virtual Private Clouds (VPCs) and on-premises networks. This approach reduces network
complexity and makes it easier to troubleshoot networking issues.
Consider your network design, including the VPCs, AWS Direct Connect, and Site-to-Site VPN
connections you want to interconnect.
