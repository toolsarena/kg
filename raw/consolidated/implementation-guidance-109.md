---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 416
---

# Implementation guidance

AWS services provide HTTPS endpoints using TLS for communication, providing encryption in
transit when communicating with the AWS APIs. Insecure HTTP protocols can be audited and
blocked in a Virtual Private Cloud (VPC) through the use of security groups. HTTP requests can also
be automatically redirected to HTTPS in Amazon CloudFront or on an Application Load Balancer.
You can use an Amazon Simple Storage Service (Amazon S3) bucket policy to restrict the ability
to upload objects through HTTP, effectively enforcing the use of HTTPS for object uploads to your
bucket(s). You have full control over your computing resources to implement encryption in transit
across your services. Additionally, you can use VPN connectivity into your VPC from an external
network or AWS Direct Connect to facilitate encryption of traffic. Verify that your clients make calls
to AWS APIs using at least TLS 1.2, as AWS has deprecated the use of earlier versions of TLS as of
February 2024. We recommend you use TLS 1.3. If you have special requirements for encryption in
transit, you can find third-party solutions available in the AWS Marketplace.


# Implementation guidance

Implementing this best practice means that there is no ambiguity about how teams work with
each other. Formal agreements codify how teams work together or support each other. Inter-team
communication channels are documented.

# Implementation guidance

Your workload’s network traffic patterns can be characterized into two categories:
• East-west traffic represents traffic flows between services that make up a workload.
• North-south traffic represents traffic flows between your workload and consumers.