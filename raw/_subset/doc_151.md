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


# Amazon S3 Multi-Region Access Points

replicates content to multiple Regions and
simplifies the workload by providing one
access point. When a Multi-Region Access

# Amazon S3 Multi-Region Access Points

replicates content to multiple Regions and
simplifies the workload by providing one
access point. When a Multi-Region Access

# Amazon S3 Use AWS Lake Formation FindMatches to find

matching records across a dataset (includin
g ones without identifiers) by using the new
FindMatches ML Transform.

# Amazon S3 Use AWS Lake Formation FindMatches to find

matching records across a dataset (includin
g ones without identifiers) by using the new
FindMatches ML Transform.

# Amazon S3 You can use Amazon S3 Lifecycle to manage

your objects throughout their lifecycle. If
your access patterns are unknown, changing,
or unpredictable, you can use Amazon S3

# Amazon S3 You can use Amazon S3 Lifecycle to manage

your objects throughout their lifecycle. If
your access patterns are unknown, changing,
or unpredictable, you can use Amazon S3

# Amazon Web Services

• Sam Mokhtari, Senior Efficiency Lead Solutions Architect, Amazon Web Services

# Amazon Web Services

• Sam Mokhtari, Senior Efficiency Lead Solutions Architect, Amazon Web Services