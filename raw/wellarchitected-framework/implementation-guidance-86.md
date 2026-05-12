---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 344
---

# Implementation guidance

You might want to allow sharing resources outside of AWS Organizations or grant a third party
access to your account. For example, a third party might provide a monitoring solution that needs
to access resources within your account. In those cases, create an IAM cross-account role with only
the privileges needed by the third party. Additionally, define a trust policy using the external ID
condition. When using an external ID, you or the third party can generate a unique ID for each
customer, third party, or tenancy. The unique ID should not be controlled by anyone but you after
it's created. The third party must implement a process to relate the external ID to the customer in a
secure, auditable, and reproduceable manner.
You can also use IAM Roles Anywhere to manage IAM roles for applications outside of AWS that use
AWS APIs.
