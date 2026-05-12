---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 622
---

# AWS Well-Architected Framework Framework

Zones alone. AWS services, with few exceptions, take advantage of this design to operate fully
independently between different Regions (also known as Regional services). A failure of an AWS
Regional service is designed not to impact the service in a different Region.
When you operate your workload in multiple Regions, you should consider additional
requirements. Because resources in different Regions are separate from and independent of
one another, you must duplicate your workload's components in each Region. This includes
foundational infrastructure, such as VPCs, in addition to compute and data services.
NOTE: When you consider a multi-Regional design, verify that your workload is capable of running
in a single Region. If you create dependencies between Regions where a component in one Region
relies on services or components in a different Region, you can increase the risk of failure and
significantly weaken your reliability posture.
