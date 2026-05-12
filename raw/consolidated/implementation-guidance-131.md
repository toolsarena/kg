---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 499
---

# Implementation guidance

When using AWS Direct Connect to connect your on-premises network to AWS, you can achieve
maximum network resiliency (SLA of 99.99%) by using separate connections that end on distinct
devices in more than one on-premises location and more than one AWS Direct Connect location.
This topology offers resilience against device failures, connectivity issues, and complete location
outages. Alternatively, you can achieve high resiliency (SLA of 99.9%) by using two individual
connections to multiple locations (each on-premises location connected to a single Direct Connect
location). This approach protects against connectivity disruptions caused by fiber cuts or device
failures and helps mitigate complete location failures. The Direct Connect Resiliency Toolkit can
assist in designing your AWS Direct Connect topology.
You can also consider AWS Site-to-Site VPN ending on an AWS Transit Gateway as a cost-effective
backup to your primary AWS Direct Connect connection. This setup enables equal-cost multipath
(ECMP) routing across multiple VPN tunnels, allowing for throughput of up to 50Gbps, even
though each VPN tunnel is capped at 1.25 Gbps. It's important to note, however, that AWS Direct
Connect is still the most effective choice for minimizing network disruptions and providing stable
connectivity.
When using VPNs over the internet to connect your cloud environment to your on-premises data
center, configure two VPN tunnels as part of a single site-to-site VPN connection. Each tunnel
should end in a different Availability Zone for high availability and use redundant hardware
to prevent on-premises device failure. Additionally, consider multiple internet connections
from various internet service providers (ISPs) at your on-premises location to avoid complete
VPN connectivity disruption due to a single ISP outage. Selecting ISPs with diverse routing and
infrastructure, especially those with separate physical paths to AWS endpoints, provides high
connectivity availability.
