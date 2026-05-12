---
title: "CloudFront distribution:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 497
---

# CloudFront distribution:

i. How caching works with CloudFront edge locations
ii. Increasing the proportion of requests that are served directly from the CloudFront caches
(cache hit ratio)
iii.Using Amazon CloudFront Origin Shield
iv.Optimizing high availability with CloudFront origin failover
5. Set up application layer protection: AWS WAF helps you protect against common web exploits
and bots that can affect availability, compromise security, or consume excessive resources. To
get a deeper understanding, review how AWS WAF works and when you are ready to implement
protections from application layer HTTP POST AND GET floods, review Getting started with
AWS WAF. You can also use AWS WAF with CloudFront see the documentation on how AWS WAF
works with Amazon CloudFront features.
6. Set up additional DDoS protection: By default, all AWS customers receive protection from
common, most frequently occurring network and transport layer DDoS attacks that target
your web site or application with AWS Shield Standard at no additional charge. For additional
protection of internet-facing applications running on Amazon EC2, Elastic Load Balancing,
Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 you can consider AWS
Shield Advanced and review examples of DDoS resilient architectures. To protect your workload
and your public endpoints from DDoS attacks review Getting started with AWS Shield Advanced.
