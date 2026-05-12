---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 416
---

# Implementation steps

• Enforce encryption in transit: Your defined encryption requirements should be based on the
latest standards and best practices and only allow secure protocols. For example, configure a
security group to only allow the HTTPS protocol to an application load balancer or Amazon EC2
instance.
• Configure secure protocols in edge services: Configure HTTPS with Amazon CloudFront and use
a security profile appropriate for your security posture and use case.
