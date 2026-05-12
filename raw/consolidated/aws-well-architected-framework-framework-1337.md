---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 773
---

# AWS Well-Architected Framework Framework

• AWS Direct Connect provides dedicated connectivity to the AWS environment, from 50 Mbps
up to 100 Gbps, using either dedicated connections or hosted connections. This gives you
managed and controlled latency and provisioned bandwidth so your workload can connect
efficiently to other environments. Using AWS Direct Connect partners, you can have end-to-
end connectivity from multiple environments, providing an extended network with consistent
performance. AWS offers scaling direct connect connection bandwidth using either native 100
Gbps, link aggregation group (LAG), or BGP equal-cost multipath (ECMP).
• The AWS Site-to-Site VPN provides a managed VPN service supporting internet protocol
security (IPsec). When a VPN connection is created, each VPN connection includes two tunnels
for high availability.
• Follow AWS documentation to choose an appropriate connectivity option:
• If you decide to use Direct Connect, select the appropriate bandwidth for your connectivity.
• If you are using an AWS Site-to-Site VPN across multiple locations to connect to an AWS
Region, use an accelerated Site-to-Site VPN connection for the opportunity to improve
network performance.
• If your network design consists of IPSec VPN connection over AWS Direct Connect, consider
using Private IP VPN to improve security and achieve segmentation. AWS Site-to-Site Private
IP VPN is deployed on top of transit virtual interface (VIF).
• AWS Direct Connect SiteLink allows creating low-latency and redundant connections between
your data centers worldwide by sending data over the fastest path between AWS Direct
Connect locations, bypassing AWS Regions.
• Validate your connectivity setup before deploying to production. Perform security and
performance testing to assure it meets your bandwidth, reliability, latency, and compliance
requirements.
• Regularly monitor your connectivity performance and usage and optimize if required.


# AWS Well-Architected Framework Framework

• AWS Transit Gateway and Scalable Security Solutions
• AWS Networking Workshops