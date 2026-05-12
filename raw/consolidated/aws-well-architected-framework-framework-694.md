---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 910
---

# AWS Well-Architected Framework Framework

are not, create new NAT gateways in the same Availability Zone as the resource to reduce cross-
AZ data transfer charges.
• Use AWS Direct Connect Direct Connect bypasses the public internet and establishes a direct,
private connection between your on-premises network and AWS. This can be more cost-effective
and consistent than transferring large volumes of data over the internet.
• Avoid transferring data across Regional boundaries: Data transfers between AWS Regions
(from one Region to another) typically incur charges. It should be a very thoughtful decision to
pursue a multi-Region path. For more detail, see Multi-Region scenarios.
• Monitor data transfer: Use Amazon CloudWatch and VPC flow logs to capture details about your
data transfer and network usage. Analyze captured network traffic information in your VPCs,
such as IP address or range going to and from network interfaces.
• Analyze your network usage: Use metering and reporting tools such as AWS Cost Explorer,
CUDOS Dashboards, or CloudWatch to understand data transfer cost of your workload.


# AWS Well-Architected Framework Framework

• Overview of Data Transfer Costs for Common Architectures
• AWS Network Optimization Tips
• Optimize performance and reduce costs for network analytics with VPC Flow Logs in Apache