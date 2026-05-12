---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 400
---

# Implementation guidance

Encryption of data at rest is a fundamental security control. To implement this control, your
workload needs a mechanism to securely store and manage the key material used to encrypt your
data at rest.
AWS offers the AWS Key Management Service (AWS KMS) to provide durable, secure, and
redundant storage for AWS KMS keys. Many AWS services integrate with AWS KMS to support
encryption of your data. AWS KMS uses FIPS 140-3 Level 3 validated hardware security modules to
protect your keys. There is no mechanism to export AWS KMS keys in plain text.
When deploying workloads using a multi-account strategy, you should keep AWS KMS keys in the
same account as the workload that uses them. This distributed model places the responsibility for
managing the AWS KMS keys with your team. In other use cases, your organization may choose
to store AWS KMS keys into a centralized account. This centralized structure requires additional
policies to enable the cross-account access required for the workload account to access keys stored
in the centralized account, but may be more applicable in use cases where a single key is shared
across multiple AWS accounts.
Regardless of where the key material is stored, you should tightly control access to the key through
the use of key policies and IAM policies. Key policies are the primary way to control access to an
AWS KMS key. Additionally, AWS KMS key grants can provide access to AWS services to encrypt and
decrypt data on your behalf. Review the guidance for access control to your AWS KMS keys.
You should monitor the use of encryption keys to detect unusual access patterns. Operations
performed using AWS managed keys and customer managed keys stored in AWS KMS can be
logged in AWS CloudTrail and should be reviewed periodically. Pay special attention to monitoring
key destruction events. To mitigate accidental or malicious destruction of key material, key
destruction events do not delete the key material immediately. Attempts to delete keys in AWS
KMS are subject to a waiting period, which defaults to 30 days and a minimum of 7 days, providing
administrators time to review these actions and roll back the request if necessary.
Most AWS services use AWS KMS in a way that is transparent to you - your only requirement is to
decide whether to use an AWS managed or customer managed key. If your workload requires the
direct use of AWS KMS to encrypt or decrypt data, you should use envelope encryption to protect
your data. The AWS Encryption SDK can provide your applications client-side encryption primitives
to implement envelope encryption and integrate with AWS KMS.
