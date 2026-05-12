---
title: "To streamline infrastructure provisioning and management, consider using infrastructure as"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 462
---

# To streamline infrastructure provisioning and management, consider using infrastructure as

code (IaC) tools like AWS CloudFormation or AWS CDK. You can use these tools to define your
infrastructure as code, which improves the consistency and repeatability of deployments across
different environments.
Consider canary deployments to validate the successful deployment of your software. Canary
deployments involve rolling out changes to a subset of instances or users before deploying to
the entire production environment. You can then monitor the impact of changes and roll back if
necessary, which minimizes the risk of widespread issues.
Follow the recommendations outlined in the Organizing Your AWS Environment Using Multiple
Accounts whitepaper. This whitepaper provides guidance on separating environments (such as
development, staging, and production) into distinct AWS accounts, which further enhances security
and isolation.
