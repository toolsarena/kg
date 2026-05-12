---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 432
---

# AWS Well-Architected Framework Framework

Setting up backups of key systems and databases are critical for recovering from a security incident
and for forensics purposes. With backups in place, you can restore your systems to their previous
safe state. On AWS, you can take snapshots of various resources. Snapshots provide you with point-
in-time backups of those resources. There are many AWS services that can support you in backup
and recovery. For detail on these services and approaches for backup and recovery, see Backup and
Recovery Prescriptive Guidance and Use backups to recover from security incidents.
Especially when it comes to situations such as ransomware, it’s critical for your backups to be well
protected. For guidance on securing your backups, see Top 10 security best practices for securing
backups in AWS. In addition to securing your backups, you should regularly test your backup and
restore processes to verify that the technology and processes you have in place work as expected.
