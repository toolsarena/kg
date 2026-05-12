---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 610
---

# AWS Well-Architected Framework Framework

Amazon S3 supports several methods of encryption of your data at rest. Using server-side
encryption, Amazon S3 accepts your objects as unencrypted data, and then encrypts them as they
are stored. Using client-side encryption, your workload application is responsible for encrypting the
data before it is sent to Amazon S3. Both methods allow you to use AWS Key Management Service
(AWS KMS) to create and store the data key, or you can provide your own key, which you are then
responsible for. Using AWS KMS, you can set policies using IAM on who can and cannot access your
data keys and decrypted data.
For Amazon RDS, if you have chosen to encrypt your databases, then your backups are encrypted
also. DynamoDB backups are always encrypted. When using AWS Elastic Disaster Recovery, all data
in transit and at rest is encrypted. With Elastic Disaster Recovery, data at rest can be encrypted
using either the default Amazon EBS encryption Volume Encryption Key or a custom customer-
managed key.
