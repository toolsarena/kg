---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 912
---

# AWS Well-Architected Framework Framework

• NAT gateways provide built-in scaling and management for reducing costs as opposed to a
standalone NAT instance. Place NAT gateways in the same Availability Zones as high traffic
instances and consider using VPC endpoints for the instances that need to access Amazon
DynamoDB or Amazon S3 to reduce the data transfer and processing costs.
• Use AWS Snow Family devices which have computing resources to collect and process data at the
edge. AWS Snow Family devices (Snowball Edge, Snowball Edge and Snowmobile) allow you to
move petabytes of data to the AWS Cloud cost effectively and offline.
