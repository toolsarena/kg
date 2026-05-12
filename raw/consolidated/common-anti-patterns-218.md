---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 975
---

# Common anti-patterns:

• You provision storage for each individual client.
• You do not detach data volume from inactive clients.
• You do not provide access to storage across platforms and systems.
Benefits of establishing this best practice: Using shared file systems or storage allows for sharing
data to one or more consumers without having to copy the data. This helps to reduce the storage
resources required for the workload.
Level of risk exposed if this best practice is not established: Medium
