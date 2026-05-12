---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 500
---

# Implementation steps

• Acquisition highly-available connectivity between AWS and your on-premises environment.
• Use multiple AWS Direct Connect connections or VPN tunnels between separately deployed
private networks.
• Use multiple Direct Connect locations for high availability.
• If using multiple AWS Regions, create redundancy in at least two of them.
• Use AWS Transit Gateway, when possible, to end your VPN connection.
• Evaluate AWS Marketplace appliances to end VPNs or extend your SD-WAN to AWS. If you
use AWS Marketplace appliances, deploy redundant instances for high availability in different
Availability Zones.
• Provide a redundant connection to your on-premises environment.
• You may need redundant connections to multiple AWS Regions to achieve your availability
needs.
• Use the Direct Connect Resiliency Toolkit to get started.
