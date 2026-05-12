---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 403
---

# Implementation guidance

Map encryption keys to data classifications within your workloads. This approach helps protect
against overly permissive access when using either a single, or very small number of encryption
keys for your data (see SEC07-BP01 Understand your data classification scheme).
AWS Key Management Service (AWS KMS) integrates with many AWS services to make it easier
to encrypt your data at rest. For example, in Amazon Elastic Compute Cloud (Amazon EC2), you
can set default encryption on accounts so that new EBS volumes are automatically encrypted.
When using AWS KMS, consider how tightly the data needs to be restricted. Default and service-
controlled AWS KMS keys are managed and used on your behalf by AWS. For sensitive data that
requires fine-grained access to the underlying encryption key, consider customer managed keys
(CMKs). You have full control over CMKs, including rotation and access management through the
use of key policies.
Additionally, services such as Amazon Simple Storage Service (Amazon S3) now encrypt all
new objects by default. This implementation provides enhanced security with no impact on
performance.
Other services, such as Amazon Elastic Compute Cloud (Amazon EC2) or Amazon Elastic File
System (Amazon EFS), support settings for default encryption. You can also use AWS Config Rules
to automatically check that you are using encryption for Amazon Elastic Block Store (Amazon EBS)
volumes, Amazon Relational Database Service (Amazon RDS) instances, Amazon S3 buckets, and
other services within your organization.
