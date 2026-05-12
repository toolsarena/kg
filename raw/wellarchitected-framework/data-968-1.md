---
title: "Data 968"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 973
---

# Data 968

| Storage service | Deduplication mechanism |
| --- | --- |
| Amazon S3 | Use AWS Lake Formation FindMatches to find
matching records across a dataset (includin
g ones without identifiers) by using the new
FindMatches ML Transform. |
| Amazon FSx | Use data deduplication on Amazon FSx for
Windows. |
| Amazon Elastic Block Store snapshots | Snapshots are incremental backups, which
means that only the blocks on the device |
