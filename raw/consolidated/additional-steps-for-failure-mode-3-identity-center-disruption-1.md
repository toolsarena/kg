---
title: "Additional steps for Failure Mode 3: Identity center disruption"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 328
---

# Additional steps for Failure Mode 3: Identity center disruption

• As detailed in Set up emergency access to the AWS Management Console, in the emergency
access AWS account, create an IAM Identity Provider to enable direct SAML federation from your
identity provider.
• Create emergency operations groups in your IdP with no members.
• Create IAM roles corresponding to the emergency operations groups in the emergency access
account.
