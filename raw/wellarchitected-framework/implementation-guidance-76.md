---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 308
---

# Implementation guidance

When you cannot rely on temporary credentials and require long-term credentials, audit
credentials to verify that defined controls like multi-factor authentication (MFA) are enforced,
rotated regularly, and have the appropriate access level.
Periodic validation, preferably through an automated tool, is necessary to verify that the correct
controls are enforced. For human identities, you should require users to change their passwords
periodically and retire access keys in favor of temporary credentials. As you move from AWS
Identity and Access Management (IAM) users to centralized identities, you can generate a credential
report to audit your users.
