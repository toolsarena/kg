---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 496
---

# AWS Well-Architected Framework Framework

Global Accelerator has a fault-isolating design that uses two static IPv4 addresses that are serviced
by independent network zones increasing the availability of your applications.
To help protect customers from DDoS attacks, AWS provides AWS Shield Standard. Shield Standard
comes automatically turned on and protects from common infrastructure (layer 3 and 4) attacks
like SYN/UDP floods and reflection attacks to support high availability of your applications
on AWS. For additional protections against more sophisticated and larger attacks (like UDP
floods), state exhaustion attacks (like TCP SYN floods), and to help protect your applications
running on Amazon Elastic Compute Cloud (Amazon EC2), Elastic Load Balancing (ELB), Amazon
CloudFront, AWS Global Accelerator, and Route 53, you can consider using AWS Shield Advanced.
For protection against Application layer attacks like HTTP POST or GET floods, use AWS WAF. AWS
WAF can use IP addresses, HTTP headers, HTTP body, URI strings, SQL injection, and cross-site
scripting conditions to determine if a request should be blocked or allowed.
