---
title: "IAM user recommendations:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 293
---

# IAM user recommendations:

• Ideally you are using IAM Identity Center or direct federation. However, you might have the
need for IAM users. In that case, set a password policy for IAM users. You can use the password
policy to define requirements such as minimum length or whether the password requires non-
alphabetic characters.
• Create an IAM policy to enforce MFA sign-in so that users are allowed to manage their own
passwords and MFA devices.
