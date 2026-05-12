---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 366
---

# Common anti-patterns:

• You take a perimeter-based approach to network security and only control traffic flow at the
boundary of your network layers.
• You assume all traffic within a network layer is authenticated and authorized.
• You apply controls for either your ingress traffic or your egress traffic, but not both.
• You rely solely on your workload components and network controls to authenticate and
authorize traffic.
Benefits of establishing this best practice: This practice helps reduce the risk of unauthorized
movement within your network and adds an extra layer of authorization to your workloads. By
performing traffic flow control, you can restrict the scope of impact of a security incident and
speed up detection and response.
Level of risk exposed if this best practice is not established: High
