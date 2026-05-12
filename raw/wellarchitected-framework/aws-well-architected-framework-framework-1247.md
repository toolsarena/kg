---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 644
---

# AWS Well-Architected Framework Framework

For example, the following are all control plane actions: launching a new compute instance,
creating block storage, and describing queue services. When you launch compute instances, the
control plane has to perform multiple tasks like finding a physical host with capacity, allocating
network interfaces, preparing local block storage volumes, generating credentials, and adding
security rules. Control planes tend to be complicated orchestration.
Desired outcome: When a resource enters an impaired state, the system is capable of
automatically or manually recovering by shifting traffic from impaired to healthy resources.
