---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 499
---

# AWS Well-Architected Framework Framework

• You rely on one ISP for VPN connectivity, which can lead to complete failures during ISP outages.
• Not implementing dynamic routing protocols like BGP, which are crucial for rerouting traffic
during network disruptions.
• You ignore the bandwidth limitations of VPN tunnels and overestimate their backup capabilities.
Benefits of establishing this best practice: By implementing redundant connectivity between
your cloud environment and your corporate or on-premises environment, the dependent services
between the two environments can communicate reliably.
Level of risk exposed if this best practice is not established: High
