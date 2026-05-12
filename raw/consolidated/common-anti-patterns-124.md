---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 505
---

# Common anti-patterns:

• You build complex network peering rules.
• You provide routes between networks that should not communicate with one another (for
example, separate workloads that have no interdependencies).
• There is ineffective governance of the hub instance.
Benefits of establishing this best practice: As the number of connected networks increases,
management and expansion of meshed connectivity becomes increasingly challenging. A mesh
architecture introduces additional challenges, such as additional infrastructure components,
configuration requirements, and deployment considerations. The mesh also introduces additional
overhead to manage and monitor the data plane and control plane components. You must think
about how to provide high availability of the mesh architecture, how to monitor the mesh health
and performance, and how to handle upgrades of the mesh components.
A hub-and-spoke model, on the other hand, establishes centralized traffic routing across multiple
networks. It provides a simpler approach to management and monitoring of the data plane and
control plane components.
Level of risk exposed if this best practice is not established: Medium
