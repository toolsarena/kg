---
title: "Backup and restore"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 688
---

# Backup and restore

Backup and restore is the least complex strategy to implement, but will require more time and
effort to restore the workload, leading to higher RTO and RPO. It is a good practice to always
make backups of your data, and copy these to another site (such as another AWS Region).
