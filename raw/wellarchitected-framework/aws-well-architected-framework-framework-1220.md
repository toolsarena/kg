---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 611
---

# AWS Well-Architected Framework Framework

• Use encryption on Amazon EBS volumes.. You can configure default encryption or specify a
unique key upon volume creation.
• Use the required Amazon DynamoDB encryption. DynamoDB encrypts all data at rest. You can
either use an AWS owned AWS KMS key or an AWS managed KMS key, specifying a key that is
stored in your account.
• Encrypt your data stored in Amazon EFS. Configure the encryption when you create your file
system.
• Configure the encryption in the source and destination Regions. You can configure encryption
at rest in Amazon S3 using keys stored in KMS, but the keys are Region-specific. You can
specify the destination keys when you configure the replication.
• Choose whether to use the default or custom Amazon EBS encryption for Elastic Disaster
Recovery. This option will encrypt your replicated data at rest on the Staging Area Subnet
disks and the replicated disks.
2. Implement least privilege permissions to access your backups. Follow best practices to limit the
access to the backups, snapshots, and replicas in accordance with security best practices.
3. Configure immutability for critical backups. For critical data, implement AWS Backup Vault Lock
or S3 Object Lock to prevent deletion or alteration during the specified retention period. For
implementation details, see AWS Backup Vault Lock.
4. Create logical separation for backup environments. Implement AWS Backup logically air-gapped
vault for critical systems requiring enhanced protection from cyber threats. For implementation
guidance, see Building cyber resiliency with AWS Backup logically air-gapped vault.
5. Implement backup validation processes. Configure AWS Backup restore testing to regularly
verify that backups are not corrupted and can be successfully restored following a cyber
incident. For more information, see Validate recovery readiness with AWS Backup restore testing.
6. Configure multi-party approval for sensitive recovery operations. For critical systems, implement
AWS Backup multi-party approval to require authorization from multiple designated approvers
before recovery can proceed. For implementation details, see Improve recovery resilience with
AWS Backup support for Multi-party approval.
