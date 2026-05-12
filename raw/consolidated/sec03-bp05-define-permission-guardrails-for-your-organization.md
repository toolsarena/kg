---
title: "SEC03-BP05 Define permission guardrails for your organization"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 331
---

# SEC03-BP05 Define permission guardrails for your organization

Use permission guardrails to reduce the scope of available permissions that can be granted to
principals. The permission policy evaluation chain includes your guardrails to determine the
effective permissions of a principal when making authorization decisions. You can define guardrails
using a layer-based approach. Apply some guardrails broadly across your entire organization and
apply others granularly to temporary access sessions.
Desired outcome: You have clear isolation of environments using separate AWS accounts.
Service control policies (SCPs) are used to define organization-wide permission guardrails.
Broader guardrails are set at the hierarchy levels closest to your organization root, and more strict
guardrails are set closer to the level of individual accounts.
