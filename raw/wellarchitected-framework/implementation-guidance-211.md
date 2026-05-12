---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 783
---

# Implementation guidance

Resources, such as Amazon EC2 instances, are placed into Availability Zones within AWS Regions,
AWS Local Zones, AWS Outposts, or AWS Wavelength zones. Selection of this location influences
network latency and throughput from a given user location. Edge services like Amazon CloudFront
and AWS Global Accelerator can also be used to improve network performance by either caching
content at edge locations or providing users with an optimal path to the workload through the
AWS global network.
Amazon EC2 provides placement groups for networking. A placement group is a logical grouping
of instances to decrease latency. Using placement groups with supported instance types and an
Elastic Network Adapter (ENA) enables workloads to participate in a low-latency, reduced jitter 25
Gbps network. Placement groups are recommended for workloads that benefit from low network
latency, high network throughput, or both.
Latency-sensitive services are delivered at edge locations using AWS global network, such as
Amazon CloudFront. These edge locations commonly provide services like content delivery
network (CDN) and domain name system (DNS). By having these services at the edge, workloads
can respond with low latency to requests for content or DNS resolution. These services also provide
geographic services, such as geotargeting of content (providing different content based on the
end users’ location) or latency-based routing to direct end users to the nearest Region (minimum
latency).
Use edge services to reduce latency and to enable content caching. Configure cache control
correctly for both DNS and HTTP/HTTPS to gain the most benefit from these approaches.
