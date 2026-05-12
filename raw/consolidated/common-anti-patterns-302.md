---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 311
---

# Common anti-patterns:

• Managing permissions for individual users and duplicating across many users.
• Defining groups at too high a level, granting overly-broad permissions.
• Defining groups at too granular a level, creating duplication and confusion about membership.
• Using groups with duplicate permissions across subsets of resources when attributes can be used
instead.
• Not managing groups, attributes, and memberships through a standardized identity provider
integrated with your AWS environments.
• Using role chaining when using AWS IAM Identity Center sessions
Level of risk exposed if this best practice is not established: Medium


# Common anti-patterns:

• Hard-coding or storing secrets in your application.
• Granting custom permissions for each user.
• Using long-lived credentials.
Level of risk exposed if this best practice is not established: High