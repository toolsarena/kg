---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 401
---

# Implementation steps

1. Determine the appropriate key management options (AWS managed or customer managed) for
the key.
a. For ease of use, AWS offers AWS owned and AWS managed keys for most services, which
provide encryption-at-rest capability without the need to manage key material or key policies.
b. When using customer managed keys, consider the default key store to provide the best
balance between agility, security, data sovereignty, and availability. Other use cases may
require the use of custom key stores with AWS CloudHSM or the external key store.
2. Review the list of services that you are using for your workload to understand how AWS KMS
integrates with the service. For example, EC2 instances can use encrypted EBS volumes, verifying
that Amazon EBS snapshots created from those volumes are also encrypted using a customer
managed key and mitigating accidental disclosure of unencrypted snapshot data.
a. How AWS services use AWS KMS
b. For detailed information about the encryption options that an AWS service offers, see the
Encryption at Rest topic in the user guide or the developer guide for the service.
3. Implement AWS KMS: AWS KMS makes it simple for you to create and manage keys and control
the use of encryption across a wide range of AWS services and in your applications.
a. Getting started: AWS Key Management Service (AWS KMS)
b. Review the best practices for access control to your AWS KMS keys.
4. Consider AWS Encryption SDK: Use the AWS Encryption SDK with AWS KMS integration when
your application needs to encrypt data client-side.
a. AWS Encryption SDK
5. Enable IAM Access Analyzer to automatically review and notify if there are overly broad AWS
KMS key policies.
a. Consider using custom policy checks to verify that a resource policy update does not grant
public access to KMS Keys.
6. Enable Security Hub CSPM to receive notifications if there are misconfigured key policies, keys
scheduled for deletion, or keys without automated rotation enabled.
7. Determine the logging level appropriate for your AWS KMS keys. Since calls to AWS KMS,
including read-only events, are logged, the CloudTrail logs associated with AWS KMS can
become voluminous.
