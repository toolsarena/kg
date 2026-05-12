---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 496
---

# Implementation steps

1. Set up highly available DNS: Amazon Route 53 is a highly available and scalable domain name
system (DNS) web service. Route 53 connects user requests to internet applications running
on AWS or on-premises. For more information, see configuring Amazon Route 53 as your DNS
service.
2. Setup health checks: When using Route 53, verify that only healthy targets are resolvable. Start
by creating Route 53 health checks and configuring DNS failover. The following aspects are
important to consider when setting up health checks:
a. How Amazon Route 53 determines whether a health check is healthy
b. Creating, updating, and deleting health checks
c. Monitoring health check status and getting notifications
d. Best practices for Amazon Route 53 DNS
3. Connect your DNS service to your endpoints.
a. When using Elastic Load Balancing as a target for your traffic, create an alias record using
Amazon Route 53 that points to your load balancer’s regional endpoint. During the creation
of the alias record, set the Evaluate target health option to Yes.
b. For serverless workloads or private APIs when API Gateway is used, use Route 53 to direct
traffic to API Gateway.
4. Decide on a content delivery network.
a. For delivering content using edge locations closer to the user, start by understanding how
CloudFront delivers content.
