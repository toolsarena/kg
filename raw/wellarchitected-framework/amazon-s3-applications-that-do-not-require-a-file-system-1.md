---
title: "Amazon S3 Applications that do not require a file system"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 976
---

# Amazon S3 Applications that do not require a file system

structure and are designed to work with
object storage can use Amazon S3 as a
massively scalable, durable, low-cost object
storage solution.
• Fetch data as needed: Copy data to or fetch data from shared file systems only as needed. As
an example, you can create an Amazon FSx for Lustre file system backed by Amazon S3 and only
load the subset of data required for processing jobs to Amazon FSx.
• Delete unneeded data: Delete data as appropriate for your usage patterns as outlined in SUS04-
BP03 Use policies to manage the lifecycle of your datasets.
• Detach inactive clients: Detach volumes from clients that are not actively using them.
