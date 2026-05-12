---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 332
---

# Implementation guidance

We recommend you use a layer-based approach to define permission guardrails for your
organization. This approach systematically reduces the maximum set of possible permissions as
additional layers are applied. This helps you grant access based on the principle of least privilege,
reducing the risk of unintended access due to policy misconfiguration.
The first step to establish permission guardrails is to isolate your workloads and environments into
separate AWS accounts. Principals from one account cannot access resources in another account
without explicit permission to do so, even when both accounts are in the same AWS organization
or under the same organizational unit (OU). You can use OUs to group accounts you want to
administer as a single unit.
The next step is to reduce the maximum set of permissions that you can grant to principals within
the member accounts of your organization. You can use service control policies (SCPs) for this
