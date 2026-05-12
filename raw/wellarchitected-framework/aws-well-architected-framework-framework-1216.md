---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 606
---

# AWS Well-Architected Framework Framework

• Not aware of all data sources for the workload and their criticality.
• Not taking backups of critical data sources.
• Taking backups of only some data sources without using criticality as a criterion.
• No defined RPO, or backup frequency cannot meet RPO.
• Not evaluating if a backup is necessary or if data can be reproduced from other sources.
Benefits of establishing this best practice: Identifying the places where backups are necessary
and implementing a mechanism to create backups, or being able to reproduce the data from an
external source improves the ability to restore and recover data during an outage.
Level of risk exposed if this best practice is not established: High
