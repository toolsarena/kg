---
title: "SEC02-BP03 Store and use secrets securely"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 298
---

# SEC02-BP03 Store and use secrets securely

A workload requires an automated capability to prove its identity to databases, resources, and
third-party services. This is accomplished using secret access credentials, such as API access keys,
passwords, and OAuth tokens. Using a purpose-built service to store, manage, and rotate these
credentials helps reduce the likelihood that those credentials become compromised.
Desired outcome: Implementing a mechanism for securely managing application credentials that
achieves the following goals:
• Identifying what secrets are required for the workload.
• Reducing the number of long-term credentials required by replacing them with short-term
credentials when possible.
• Establishing secure storage and automated rotation of remaining long-term credentials.
• Auditing access to secrets that exist in the workload.
• Continual monitoring to verify that no secrets are embedded in source code during the
development process.
