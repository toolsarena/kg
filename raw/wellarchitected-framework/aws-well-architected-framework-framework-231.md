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
