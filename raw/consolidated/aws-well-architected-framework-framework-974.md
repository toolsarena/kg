---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 297
---

# AWS Well-Architected Framework Framework

• Consider granting the IAM user only the AssumeRole operation for one specific role.
Depending on the on-premise architecture, this approach helps isolate and secure the long-
term IAM credentials.
• Limit the allowed network sources and IP addresses in the IAM role trust policy.
• Monitor usage and set up alerts for unused permissions or misuse (using AWS CloudWatch Logs
metric filters and alarms).
• Enforce permission boundaries (service control policies (SCPs) and permission boundaries
complement each other - SCPs are coarse-grained, while permission boundaries are fine-
grained).
• Implement a process to provision and securely store (in an on-premise vault) the credentials.
