---
title: "Amazon RDS or Amazon"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 301
---

# Amazon RDS or Amazon

Aurora. In addition, some RDS
database types can use IAM
roles instead of passwords
for some use cases (for more
detail, see IAM database
authentication).
OAuth tokens Secret tokens – plain text Rotate: Store tokens in
string AWS Secrets Manager and
configure automated rotation.
API tokens and keys Secret tokens – plain text Rotate: Store in AWS Secrets
string Manager and establish
automated rotation if
possible.
A common anti-pattern is embedding IAM access keys inside source code, configuration files,
or mobile apps. When an IAM access key is required to communicate with an AWS service, use
temporary (short-term) security credentials. These short-term credentials can be provided through
IAM roles for EC2 instances, execution roles for Lambda functions, Cognito IAM roles for mobile
user access, and IoT Core policies for IoT devices. When interfacing with third parties, prefer
delegating access to an IAM role with the necessary access to your account's resources rather than
configuring an IAM user and sending the third party the secret access key for that user.
There are many cases where the workload requires the storage of secrets necessary to interoperate
with other services and resources. AWS Secrets Manager is purpose built to securely manage
