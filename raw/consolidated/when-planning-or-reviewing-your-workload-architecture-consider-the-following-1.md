---
title: "When planning or reviewing your workload architecture, consider the following:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 909
---

# When planning or reviewing your workload architecture, consider the following:

• Use VPC endpoints within AWS: VPC endpoints allow for private connections between your VPC
and supported AWS services. This allows you to avoid using the public internet, which can lead to
data transfer costs.
• Use a NAT gateway: Use a NAT gateway so that instances in a private subnet can connect to
the internet or to the services outside your VPC. Check whether the resources behind the NAT
gateway that send the most traffic are in the same Availability Zone as the NAT gateway. If they
