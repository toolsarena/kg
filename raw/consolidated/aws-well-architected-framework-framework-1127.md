---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 494
---

# AWS Well-Architected Framework Framework

Desired outcome: It is critical to plan, build, and operationalize highly available network
connectivity for your public endpoints. If your workload becomes unreachable due to a loss in
connectivity, even if your workload is running and available, your customers will see your system
as down. By combining the highly available and resilient network connectivity for your workload’s
public endpoints, along with a resilient architecture for your workload itself, you can provide the
best possible availability and service level for your customers.
AWS Global Accelerator, Amazon CloudFront, Amazon API Gateway, AWS Lambda Function URLs,
AWS AppSync APIs, and Elastic Load Balancing (ELB) all provide highly available public endpoints.
Amazon Route 53 provides a highly available DNS service for domain name resolution to verify
that your public endpoint addresses can be resolved.
You can also evaluate AWS Marketplace software appliances for load balancing and proxying.
