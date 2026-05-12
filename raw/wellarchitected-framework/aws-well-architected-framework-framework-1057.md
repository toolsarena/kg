---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 404
---

# AWS Well-Architected Framework Framework

AWS also provides options for client-side encryption, allowing you to encrypt data prior to
uploading it to the cloud. The AWS Encryption SDK provides a way to encrypt your data using
envelope encryption. You provide the wrapping key, and the AWS Encryption SDK generates a
unique data key for each data object it encrypts. Consider AWS CloudHSM if you need a managed
single-tenant hardware security module (HSM). AWS CloudHSM allows you to generate, import,
and manage cryptographic keys on a FIPS 140-2 level 3 validated HSM. Some use cases for AWS
CloudHSM include protecting private keys for issuing a certificate authority (CA), and turning on
transparent data encryption (TDE) for Oracle databases. The AWS CloudHSM Client SDK provides
software that allows you to encrypt data client side using keys stored inside AWS CloudHSM prior
to uploading your data into AWS. The Amazon DynamoDB Encryption Client also allows you to
encrypt and sign items prior to upload into a DynamoDB table.
