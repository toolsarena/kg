---
title: "REL10-BP01 Deploy the workload to multiple locations"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 619
---

# REL10-BP01 Deploy the workload to multiple locations

Distribute workload data and resources across multiple Availability Zones or, where necessary,
across AWS Regions.
A fundamental principle for service design in AWS is to avoid single points of failure, including
the underlying physical infrastructure. AWS provides cloud computing resources and services
globally across multiple geographic locations called Regions. Each Region is physically and
logically independent and consists of three or more Availability Zones (AZs). Availability Zones are
geographically close to each other but are physically separated and isolated. When you distribute
your workloads among Availability Zones and Regions, you mitigate the risk of threats such as fires,
floods, weather-related disasters, earthquakes, and human error.
Create a location strategy to provide high availability that is appropriate for your workloads.
Desired outcome: Production workloads are distributed among multiple Availability Zones (AZs) or
Regions to achieve fault tolerance and high availability.
