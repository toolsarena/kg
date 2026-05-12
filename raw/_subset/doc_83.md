---
title: "4. For inbound web traffic solutions:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 371
---

# 4. For inbound web traffic solutions:

a. To configure AWS WAF, start by configuring a web access control list (web ACL). The web ACL
is a collection of rules with a serially processed default action (ALLOW or DENY) that defines
how your WAF handles traffic. You can create your own rules and groups or use AWS managed
rule groups in your web ACL.
b. Once your web ACL is configured, associate the web ACL with an AWS resource (like an
Application Load Balancer, API Gateway REST API, or CloudFront distribution) to begin
protecting web traffic.
