---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 979
---

# Implementation steps

• Classify data: Implement data classification policy as outlined in SUS04-BP01 Implement a data
classification policy.
• Design a backup strategy: Use the criticality of your data classification and design backup
strategy based on your recovery time objective (RTO) and recovery point objective (RPO). Avoid
backing up non-critical data.
• Exclude data that can be easily recreated.
• Exclude ephemeral data from your backups.
• Exclude local copies of data, unless the time required to restore that data from a common
location exceeds your service-level agreements (SLAs).
• Use automated backup: Use an automated solution or managed service to back up business-
critical data.
• AWS Backup is a fully-managed service that makes it easy to centralize and automate data
protection across AWS services, in the cloud, and on premises. For hands-on guidance on how
