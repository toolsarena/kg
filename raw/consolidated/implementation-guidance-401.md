---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 397
---

# Implementation guidance

Data within a workload is often dynamic. The form it takes when entering your workload
environment can be different from when it is stored or used in business logic, reporting, analytics,
or machine learning. In addition, the value of data can change over time. Some data is temporal in
nature and loses value as it gets older. Consider how these changes to your data impact evaluation
under your data classification scheme and associated controls. Where possible, use an automated
lifecycle mechanism, such as Amazon S3 lifecycle policies and the Amazon Data Lifecycle Manager,
to configure your data retention, archiving, and expiration processes. For data stored in DynamoDB,
you can use the Time To Live (TTL) feature to define a per-item expiration timestamp.
Distinguish between data that is available for use, and data that is stored as a backup. Consider
using AWS Backup to automate the backup of data across AWS services. A mazon EBS snapshots
provide a way to copy an EBS volume and store it using S3 features, including lifecycle, data
protection, and access to protection mechanisms. Two of these mechanisms are S3 Object Lock
and AWS Backup Vault Lock, which can provide you with additional security and control over your
backups. Manage clear separation of duties and access for backups. Isolate backups at the account
level to maintain separation from the affected environment during an event.
Another aspect of lifecycle management is recording the history of data as it progresses through
your workload, called data provenance tracking. This can give confidence that you know where
the data came from, any transformations performed, what owner or process made those changes,
and when. Having this history helps with troubleshooting issues and investigations during
potential security events. For example, you can log metadata about transformations in an Amazon
DynamoDB table. Within a data lake, you can keep copies of transformed data in different
S3 buckets for each data pipeline stage. Store schema and timestamp information in an AWS
Glue Data Catalog. Regardless of your solution, consider the requirements of your end users to
determine the appropriate tooling you need to report on your data provenance. This will help you
determine how to best track your provenance.
