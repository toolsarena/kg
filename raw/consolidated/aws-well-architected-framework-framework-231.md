---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 309
---

# AWS Well-Architected Framework Framework

We also recommend that you enforce and monitor MFA in your identity provider. You can set up
AWS Config Rules, or use AWS Security Hub CSPM Security Standards, to monitor if users have
configured MFA. Consider using IAM Roles Anywhere to provide temporary credentials for machine
identities. In situations when using IAM roles and temporary credentials is not possible, frequent
auditing and rotating access keys is necessary.


# AWS Well-Architected Framework Framework

a. Following the guidance in SEC02-BP04 Rely on a centralized identity provider, you can
determine whether you need to define groups and attributes within your identity provider,
within IAM Identity Center, or using IAM user groups in a specific account.

# AWS Well-Architected Framework Framework

c. Regularly review and update your group and attribute structure as your organization's needs
evolve to ensure optimal permissions management.