---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 899
---

# AWS Well-Architected Framework Framework

When you architect your solutions, a best practice is to seek to place computing resources closer to
users to provide lower latency and strong data sovereignty. Select the geographic location based
on your business, data privacy, performance, and security requirements. For applications with
global end users, use multiple locations.
Use Regions that provide lower prices for AWS services to deploy your workloads if you have no
obligations in data privacy, security and business requirements. For example, if your default Region
is Asia Pacific (Sydney) (ap-southwest-2), and if there are no restrictions (data privacy, security,
for example) to use other Regions, deploying non-critical (development and test) Amazon EC2
instances in US East (N. Virginia) (us-east-1) will cost you less.
