---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 303
---

# AWS Well-Architected Framework Framework

i. Serverless Lambda functions can use a language-agnostic Lambda extension.
ii. For EC2 instances or containers, AWS provides example client-side code for retrieving
secrets from Secrets Manager in several popular programming languages.
4. Periodically review your code base and re-scan to verify no new secrets have been added to the
code.
a. Consider using a tool such as git-secrets to prevent committing new secrets to your source
code repository.
5. Monitor Secrets Manager activity for indications of unexpected usage, inappropriate secret
access, or attempts to delete secrets.
6. Reduce human exposure to credentials. Restrict access to read, write, and modify credentials to
an IAM role dedicated for this purpose, and only provide access to assume the role to a small
subset of operational users.


# AWS Well-Architected Framework Framework

• Securing Secrets for Hybrid Workloads Using AWS Secrets Manager