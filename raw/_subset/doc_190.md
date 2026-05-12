---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 334
---

# AWS Well-Architected Framework Framework

A more granular step is to implement privileged access management (PAM) and temporary
elevated access management (TEAM) techniques. One example of PAM is to require principals to
perform multi-factor authentication before taking privileged actions. For more information, see
Configuring MFA-protected API access. TEAM requires a solution that manages the approval and
timeframe that a principal is allowed to have elevated access. One approach is to temporarily add
the principal to the role trust policy for an IAM role that has elevated access. Another approach
is to, under normal operation, scope down the permissions granted to a principal by an IAM role
using a session policy, and then temporarily lift this restriction during the approved time window.
To learn more about solutions that AWS and select partners validated, see Temporary elevated
access.


# AWS Well-Architected Framework Framework

• Establish permissions guardrails using data perimeters
• Policy evaluation logic