---
title: "Cyber resilience considerations"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 610
---

# Cyber resilience considerations

To enhance backup security against cyber threats, consider implementing these additional controls
besides encryption:
• Implement immutability using AWS Backup Vault Lock or Amazon S3 Object Lock to prevent
backup data from being altered or deleted during its retention period, protecting against
ransomware and malicious deletion.
• Establish logical isolation between production and backup environments with AWS Backup
logically air-gapped vault for critical systems, creating separation that helps prevent compromise
of both environments simultaneously.
• Validate backup integrity regularly using AWS Backup restore testing to verify that backups are
not corrupted and can be successfully restored following a cyber incident.
• Implement multi-party approval for critical recovery operations using AWS Backup multi-party
approval to prevent unauthorized or malicious recovery attempts by requiring authorization
from multiple designated approvers.
