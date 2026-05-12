---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 288
---

# Common anti-patterns:

• You don't subscribe to AWS blogs and RSS feeds to learn of relevant new features and services
quickly
• You rely on news and updates about security services and features from second-hand sources
• You don't encourage AWS users in your organization to stay informed on the latest updates


# Common anti-patterns:

• Not enforcing a strong password policy for your identities including complex passwords and

# Common anti-patterns:

• Developers using long-term access keys from IAM users rather than obtaining temporary
credentials from the CLI using federation.
• Developers embedding long-term access keys in their code and uploading that code to public Git
repositories.

# Common anti-patterns:

• Not rotating credentials.
• Storing long-term credentials in source code or configuration files.
• Storing credentials at rest unencrypted.