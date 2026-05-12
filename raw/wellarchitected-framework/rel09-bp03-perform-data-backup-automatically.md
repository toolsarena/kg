---
title: "REL09-BP03 Perform data backup automatically"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 612
---

# REL09-BP03 Perform data backup automatically

Configure backups to be taken automatically based on a periodic schedule informed by the
Recovery Point Objective (RPO), or by changes in the dataset. Critical datasets with low data loss
requirements need to be backed up automatically on a frequent basis, whereas less critical data
where some loss is acceptable can be backed up less frequently.
Desired outcome: An automated process that creates backups of data sources at an established
cadence.
