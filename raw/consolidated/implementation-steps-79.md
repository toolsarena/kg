---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 404
---

# Implementation steps

• Configure default encryption for new Amazon EBS volumes: Specify that you want all newly
created Amazon EBS volumes to be created in encrypted form, with the option of using the
default key provided by AWS or a key that you create.
• Configure encrypted Amazon Machine Images (AMIs): Copying an existing AMI with encryption
configured will automatically encrypt root volumes and snapshots.
• Configure Amazon RDS encryption: Configure encryption for your Amazon RDS database
clusters and snapshots at rest by using the encryption option.
• Create and configure AWS KMS keys with policies that limit access to the appropriate
principals for each classification of data: For example, create one AWS KMS key for encrypting
production data and a different key for encrypting development or test data. You can also
provide key access to other AWS accounts. Consider having different accounts for your
development and production environments. If your production environment needs to decrypt
artifacts in the development account, you can edit the CMK policy used to encrypt the
development artifacts to give the production account the ability to decrypt those artifacts. The
production environment can then ingest the decrypted data for use in production.
• Configure encryption in additional AWS services: For other AWS services you use, review the
security documentation for that service to determine the service's encryption options.
