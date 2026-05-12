---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 417
---

# AWS Well-Architected Framework Framework

• Use a VPN for external connectivity: Consider using an IPsec VPN for securing point-to-point or
network-to-network connections to help provide both data privacy and integrity.
• Configure secure protocols in load balancers: Select a security policy that provides the
strongest cipher suites supported by the clients that will be connecting to the listener. Create an
HTTPS listener for your Application Load Balancer.
• Configure secure protocols in Amazon Redshift: Configure your cluster to require a secure
socket layer (SSL) or transport layer security (TLS) connection.
• Configure secure protocols: Review AWS service documentation to determine encryption-in-
transit capabilities.
• Configure secure access when uploading to Amazon S3 buckets: Use Amazon S3 bucket policy
controls to enforce secure access to data.
• Consider using AWS Certificate Manager: ACM allows you to provision, manage, and deploy
public TLS certificates for use with AWS services.
• Consider using AWS Private Certificate Authority for private PKI needs: AWS Private CA allows
you to create private certificate authority (CA) hierarchies to issue end-entity X.509 certificates
that can be used to create encrypted TLS channels.
