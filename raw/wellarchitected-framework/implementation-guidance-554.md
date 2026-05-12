---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 898
---

# Implementation guidance

The AWS Cloud Infrastructure is global, hosted in multiple locations world-wide, and built around
AWS Regions, Availability Zones, Local Zones, AWS Outposts, and Wavelength Zones. A Region
is a physical location in the world and each Region is a separate geographic area where AWS has
multiple Availability Zones. Availability Zones which are multiple isolated locations within each
Region consist of one or more discrete data centers, each with redundant power, networking, and
connectivity.
Each AWS Region operates within local market conditions, and resource pricing is different in each
Region due to differences in the cost of land, fiber, electricity, and taxes, for example. Choose
a specific Region to operate a component of or your entire solution so that you can run at the
lowest possible price globally. Use AWS Calculator to estimate the costs of your workload in various
Regions by searching services by location type (Region, wave length zone and local zone) and
Region.
