---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 600
---

# Implementation steps

• Disallow the in-place modification of running infrastructure resources.
• You can use AWS Identity and Access Management (IAM) to specify who or what can access
services and resources in AWS, centrally manage fine-grained permissions, and analyze access
to refine permissions across AWS.
• Automate the deployment of infrastructure resources to increase reproducibility and minimize
the potential of human error.
• As described in the Introduction to DevOps on AWS whitepaper, automation is a cornerstone
with AWS services and is internally supported in all services, features, and offerings.
• Prebaking your Amazon Machine Image (AMI) can speed up the time to launch them.
EC2 Image Builder is a fully managed AWS service that helps you automate the creation,
maintenance, validation, sharing, and deployment of customized, secure, and up-to-date Linux
or Windows custom AMI.
• Some of the services that support automation are:
