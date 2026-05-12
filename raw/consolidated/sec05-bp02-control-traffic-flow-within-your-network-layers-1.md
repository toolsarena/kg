---
title: "SEC05-BP02 Control traffic flow within your network layers"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 366
---

# SEC05-BP02 Control traffic flow within your network layers

Within the layers of your network, use further segmentation to restrict traffic only to the flows
necessary for each workload. First, focus on controlling traffic between the internet or other
external systems to a workload and your environment (north-south traffic). Afterwards, look at
flows between different components and systems (east-west traffic).
Desired outcome: You permit only the network flows necessary for the components of your
workloads to communicate with each other and their clients and any other services they depend
on. Your design factors in considerations such as public compared to private ingress and egress,
data classification, regional regulations, and protocol requirements. Wherever possible, you favor
point-to-point flows over network peering as part of a principle of least privilege design.
