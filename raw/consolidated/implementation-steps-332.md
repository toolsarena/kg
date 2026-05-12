---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 414
---

# Implementation steps

1. Determine the relevant AWS services required for your use case:
• Many use cases can leverage the existing AWS public key infrastructure using AWS Certificate
Manager. ACM can be used to deploy TLS certificates for web servers, load balancers, or other
uses for publicly trusted certificates.
• Consider AWS Private CA when you need to establish your own private certificate authority
hierarchy or need access to exportable certificates. ACM can then be used to issue many types
of end-entity certificates using the AWS Private CA.
• For use cases where certificates must be provisioned at scale for embedded Internet of things
(IoT) devices, consider AWS IoT Core.
• Consider using native mTLS functionality in services like Amazon API Gateway or Application
Load Balancer.
