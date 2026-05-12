---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 368
---

# Implementation steps

1. Identify the required data flows between the components of your workloads.
2. Apply multiple controls with a defense-in-depth approach for both inbound and outbound
traffic, including the use of security groups, and route tables.
3. Use firewalls to define fine-grained control over network traffic in, out, and across your VPCs,
such as the Route 53 Resolver DNS Firewall, AWS Network Firewall, and AWS WAF. Consider
using the AWS Firewall Manager for centrally configuring and managing your firewall rules
across your organization.
