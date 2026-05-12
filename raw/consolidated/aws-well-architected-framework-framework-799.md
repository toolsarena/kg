---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 66
---

# AWS Well-Architected Framework Framework

Remove unneeded or redundant data: Duplicate data only when necessary to minimize total
storage consumed. Use backup technologies that deduplicate data at the file and block level. Limit
the use of Redundant Array of Independent Drives (RAID) configurations except where required to
meet SLAs.
Use shared file systems or object storage to access common data: Adopt shared storage and
single sources of truth to avoid data duplication and reduce the total storage requirements
of your workload. Fetch data from shared storage only as needed. Detach unused volumes to
release resources. Minimize data movement across networks: Use shared storage and access data
from Regional data stores to minimize the total networking resources required to support data
movement for your workload.
Back up data only when difficult to recreate: To minimize storage consumption, only back up data
that has business value or is required to satisfy compliance requirements. Examine backup policies
and exclude ephemeral storage that doesn’t provide value in a recovery scenario.
