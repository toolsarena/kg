---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 508
---

# Implementation guidance

Make use of an IPAM, such as the Amazon VPC IP Address Manager, to monitor and manage your
CIDR use. Several IPAMs are also available from the AWS Marketplace. Evaluate your potential
usage on AWS, add CIDR ranges to existing VPCs, and create VPCs to allow planned growth in
usage.


# Implementation guidance

Choose your architecture type based on how you will segment your workload. Choose an SOA or
microservices architecture (or in some rare cases, a monolithic architecture). Even if you choose