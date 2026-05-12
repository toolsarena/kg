---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 319
---

# Implementation steps

• Implement least privilege policies: Assign access policies with least privilege to IAM groups and
roles to reflect the user's role or function that you have defined.
• Isolate development and production environments through separate AWS accounts: Use
separate AWS accounts for development and production environments, and control access
between them using service control policies, resource policies, and identity policies.
• Base policies on API usage: One way to determine the needed permissions is to review AWS
CloudTrail logs. You can use this review to create permissions tailored to the actions that the user
actually performs within AWS. IAM Access Analyzer can automatically generate an IAM policy
based on access activity. You can use IAM Access Advisor at the organization or account level to
track the last accessed information for a particular policy.
• Consider using AWS managed policies for job functions: When you begin to create fine-grained
permissions policies, it can be helpful to use AWS managed policies for common job roles, such
