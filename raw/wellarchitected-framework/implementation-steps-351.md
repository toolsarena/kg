---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 506
---

# Implementation steps

1. Plan your network. Determine which networks you want to connect, and verify that they don't
share overlapping CIDR ranges.
2. Create an AWS Transit Gateway and attach your VPCs.
3. If needed, create VPN connections or Direct Connect gateways, and associate them with the
Transit Gateway.
4. Define how traffic is routed between the connected VPCs and other connections through
configuration of your Transit Gateway route tables.
5. Use Amazon CloudWatch to monitor and adjust configurations as necessary for performance
and cost optimization.
