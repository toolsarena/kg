---
title: "REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 501
---

# REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability

Amazon VPC IP address ranges must be large enough to accommodate workload requirements,
including factoring in future expansion and allocation of IP addresses to subnets across Availability
Zones. This includes load balancers, EC2 instances, and container-based applications.
When you plan your network topology, the first step is to define the IP address space itself. Private
IP address ranges (following RFC 1918 guidelines) should be allocated for each VPC. Accommodate
the following requirements as part of this process:
• Allow IP address space for more than one VPC per Region.
• Within a VPC, allow space for multiple subnets so that you can cover multiple Availability Zones.
• Consider leaving unused CIDR block space within a VPC for future expansion.
• Ensure that there is IP address space to meet the needs of any transient fleets of Amazon EC2
instances that you might use, such as Spot Fleets for machine learning, Amazon EMR clusters, or
Amazon Redshift clusters. Similar consideration should be given to Kubernetes clusters, such as
Amazon Elastic Kubernetes Service (Amazon EKS), as each Kubernetes pod is assigned a routable
address from the VPC CIDR block by default.
• Note that the first four IP addresses and the last IP address in each subnet CIDR block are
reserved and not available for your use.
