---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 911
---

# Implementation guidance

There are various AWS services that can help you to optimize your network data transfer usage.
Depending on your workload components, type, and cloud architecture, these services can assist
you in compression, caching, and sharing and distribution of your traffic on the cloud.
• Amazon CloudFront is a global content delivery network that delivers data with low latency and
high transfer speeds. It caches data at edge locations across the world, which reduces the load
on your resources. By using CloudFront, you can reduce the administrative effort in delivering
content to large numbers of users globally with minimum latency. The security savings bundle
can help you to save up to 30% on your CloudFront usage if you plan to grow your usage over
time.
• AWS Direct Connect allows you to establish a dedicated network connection to AWS. This can
reduce network costs, increase bandwidth, and provide a more consistent network experience
than internet-based connections.
• Site-to-Site VPN allows you to establish a secure and private connection between your private
network and the AWS global network. It is ideal for small offices or business partners because it
provides simplified connectivity, and it is a fully managed and elastic service.
• VPC Endpoints allow connectivity between AWS services over private networking and can be
used to reduce public data transfer and NAT gateway costs. Gateway VPC endpoints have no
hourly charges, and support Amazon S3 and Amazon DynamoDB. Interface VPC endpoints are
provided by AWS PrivateLink and have an hourly fee and per-GB usage cost.
