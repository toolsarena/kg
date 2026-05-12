---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 613
---

# Implementation guidance

AWS Backup can be used to create automated data backups of various AWS data sources.
Amazon RDS instances can be backed up almost continuously every five minutes and Amazon
S3 objects can be backed up almost continuously every fifteen minutes, providing for point-in-
time recovery (PITR) to a specific point in time within the backup history. For other AWS data
sources, such as Amazon EBS volumes, Amazon DynamoDB tables, or Amazon FSx file systems,
AWS Backup can run automated backup as frequently as every hour. These services also offer
native backup capabilities. AWS services that offer automated backup with point-in-time recovery
include Amazon DynamoDB, Amazon RDS, and Amazon Keyspaces (for Apache Cassandra) – these
can be restored to a specific point in time within the backup history. Most other AWS data storage
services offer the ability to schedule periodic backups, as frequently as every hour.
Amazon RDS and Amazon DynamoDB offer continuous backup with point-in-time recovery.
Amazon S3 versioning, once turned on, is automatic. Amazon Data Lifecycle Manager can be used
to automate the creation, copy and deletion of Amazon EBS snapshots. It can also automate the
creation, copy, deprecation and deregistration of Amazon EBS-backed Amazon Machine Images
(AMIs) and their underlying Amazon EBS snapshots.
AWS Elastic Disaster Recovery provides continuous block-level replication from the source
environment (on-premises or AWS) to the target recovery region. Point-in-time Amazon EBS
snapshots are automatically created and managed by the service.
For a centralized view of your backup automation and history, AWS Backup provides a fully
managed, policy-based backup solution. It centralizes and automates the back up of data across
multiple AWS services in the cloud as well as on premises using the AWS Storage Gateway.
In additional to versioning, Amazon S3 features replication. The entire S3 bucket can be
automatically replicated to another bucket in the same, or a different AWS Region.
