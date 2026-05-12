---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 623
---

# AWS Well-Architected Framework Framework

Application Recovery Controller (ARC) to provide a highly-available routing control for manually re-
routing traffic as needed.
Even if you choose not to operate in multiple Regions for high availability, consider multiple
Regions as part of your disaster recovery (DR) strategy. If possible, replicate your workload's
infrastructure components and data in a warm standby or pilot light configuration in a secondary
Region. In this design, you replicate baseline infrastructure from the primary Region such as
VPCs, Auto Scaling groups, container orchestrators, and other components, but you configure
the variable-sized components in the standby Region (such as the number of EC2 instances and
database replicas) to be a minimally-operable size. You also arrange for continuous data replication
from the primary Region to the standby Region. If an incident occurs, you can then scale out, or
grow, the resources in the standby Region, and then promote it to become the primary Region.
