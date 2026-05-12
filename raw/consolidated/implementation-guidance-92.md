---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 366
---

# Implementation guidance

While network layers help establish the boundaries around components of your workload that
serve a similar function, data sensitivity level, and behavior, you can create a much finer-grained
level of traffic control by using techniques to further segment components within these layers
that follows the principle of least privilege. Within AWS, network layers are primarily defined using
subnets according to IP address ranges within an Amazon VPC. Layers can also be defined using
different VPCs, such as for grouping microservice environments by business domain. When using
multiple VPCs, mediate routing using an AWS Transit Gateway. While this provides traffic control
at a Layer 4 level (IP address and port ranges) using security groups and route tables, you can gain
