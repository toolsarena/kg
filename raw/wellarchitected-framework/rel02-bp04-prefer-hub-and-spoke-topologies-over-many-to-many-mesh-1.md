---
title: "REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 504
---

# REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh

When connecting multiple private networks, such as Virtual Private Clouds (VPCs) and on-premises
networks, opt for a hub-and-spoke topology over a meshed one. Unlike meshed topologies, where
each network connects directly to the others and increases the complexity and management
overhead, the hub-and-spoke architecture centralizes connections through a single hub. This
centralization simplifies the network structure and enhances its operability, scalability, and control.
AWS Transit Gateway is a managed, scalable, and highly-available service designed for construction
of hub-and-spoke networks on AWS. It serves as the central hub of your network that provides
network segmentation, centralized routing, and the simplified connection to both cloud and on-
premises environments. The following figure illustrates how you can use AWS Transit Gateway to
build your hub-and-spoke topology.
