---
title: "Best practices"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 605
---

# Best practices

• REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data
from sources
• REL09-BP02 Secure and encrypt backups
• REL09-BP03 Perform data backup automatically
• REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes
REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data
from sources
Understand and use the backup capabilities of the data services and resources used by the
workload. Most services provide capabilities to back up workload data.
Desired outcome: Data sources have been identified and classified based on criticality. Then,
establish a strategy for data recovery based on the RPO. This strategy involves either backing up
these data sources, or having the ability to reproduce data from other sources. In the case of data
loss, the strategy implemented allows recovery or the reproduction of data within the defined RPO
and RTO.
