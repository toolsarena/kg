---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 907
---

# Implementation guidance

When designing a solution in the cloud, data transfer fees are usually neglected due to habits
of designing architecture using on-premises data centers or lack of knowledge. Data transfer
charges in AWS are determined by the source, destination, and volume of traffic. Factoring in these
fees during the design phase can lead to cost savings. Understanding where the data transfer
occurs in your workload, the cost of the transfer, and its associated benefit is very important to
accurately estimate total cost of ownership (TCO). This allows you to make an informed decision to
modify or accept the architectural decision. For example, you may have a Multi-Availability Zone
configuration where you replicate data between the Availability Zones.
You model the components of services which transfer the data in your workload, and decide that
this is an acceptable cost (similar to paying for compute and storage in both Availability Zones) to
achieve the required reliability and resilience. Model the costs over different usage levels. Workload
usage can change over time, and different services may be more cost effective at different levels.
While modeling your data transfer, think about how much data is ingested and where that
data comes from. Additionally, consider how much data is processed and how much storage or
compute capacity is needed. During modeling, follow networking best practices for your workload
architecture to optimize your potential data transfer costs.
The AWS Pricing Calculator can help you see estimated costs for specific AWS services and
expected data transfer. If you have a workload already running (for test purposes or in a pre-
production environment), use AWS Cost Explorer or AWS Cost and Usage Report (CUR) to
understand and model your data transfer costs. Configure a proof of concept (PoC) or test your
workload, and run a test with a realistic simulated load. You can model your costs at different
workload demands.
