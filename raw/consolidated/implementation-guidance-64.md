---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 267
---

# Implementation guidance

AWS accounts provide a security isolation boundary between workloads or resources that operate
at different sensitivity levels. AWS provides tools to manage your cloud workloads at scale through
a multi-account strategy to leverage this isolation boundary. For guidance on the concepts,
patterns, and implementation of a multi-account strategy on AWS, see Organizing Your AWS
Environment Using Multiple Accounts.
When you have multiple AWS accounts under central management, your accounts should be
organized into a hierarchy defined by layers of organizational units (OUs). Security controls
can then be organized and applied to the OUs and member accounts, establishing consistent
preventative controls on member accounts in the organization. The security controls are inherited,
