---
title: "OPS05-BP08 Use multiple environments"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 168
---

# OPS05-BP08 Use multiple environments

Use multiple environments to experiment, develop, and test your workload. Use increasing levels
of controls as environments approach production to gain confidence your workload operates as
intended when deployed.
Desired outcome: You have multiple environments that reflect your compliance and governance
needs. You test and promote code through environments on your path to production.
1. Your organization does this through the establishment of a landing zone, which provides
governance, controls, account automations, networking, security, and operational observability.
Manage these landing zone capabilities by using multiple environments. A common example
is a sandbox organization for developing and testing changes to an AWS Control Tower-based
landing zone, which includes AWS IAM Identity Center and policies such as service control
policies (SCPs). All of these elements can significantly impact the access to and operation of
AWS accounts within the landing zone.
2. In addition to these services, your teams extend the landing zones capabilites with solutions
published by AWS and AWS partners or as custom solutions developed within your organization.
