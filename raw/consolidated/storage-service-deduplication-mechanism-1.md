---
title: "Storage service Deduplication mechanism"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 974
---

# Storage service Deduplication mechanism

that have changed after your most recent
snapshot are saved.
• Use lifecycle policies: Use lifecycle policies to automate unneeded data deletion. Use native
service features like Amazon DynamoDB Time To Live, Amazon S3 Lifecycle, or Amazon
CloudWatch log retention for deletion.
• Use data virtualization: Use data virtualization capabilities on AWS to maintain data at its
source and avoid data duplication.
• Cloud Native Data Virtualization on AWS
• Optimize Data Pattern Using Amazon Redshift Data Sharing
• Use incremental backup: Use backup technology that can make incremental backups.
• Use native durability: Leverage the durability of Amazon S3 and replication of Amazon EBS to
meet your durability goals instead of self-managed technologies (such as a redundant array of
independent disks (RAID)).
• Use efficient logging: Centralize log and trace data, deduplicate identical log entries, and
establish mechanisms to tune verbosity when needed.
• Use efficient caching: Pre-populate caches only where justified.
• Establish cache monitoring and automation to resize the cache accordingly.
• Remove old version assets: Remove out-of-date deployments and assets from object stores and
edge caches when pushing new versions of your workload.
