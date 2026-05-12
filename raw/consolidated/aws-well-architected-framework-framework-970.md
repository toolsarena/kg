---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 292
---

# AWS Well-Architected Framework Framework

the centralized IdP or using AWS IAM Identity Center) when authenticating to AWS. In this case,
establish a secure sign-in process with your identity provider or Microsoft Active Directory.
When you first open an AWS account, you begin with an AWS account root user. You should only
use the account root user to set up access for your users (and for tasks that require the root user).
It's important to turn on multi-factor authentication (MFA) for the account root user immediately
after opening your AWS account and to secure the root user using the AWS best practice guide.
AWS IAM Identity Center is designed for workforce users, and you can create and manage user
identities within the service and secure the sign-in process with MFA. AWS Cognito, on the other
hand, is designed for customer identity and access management (CIAM), which provides user pools
and identity providers for external user identities in your applications.
If you create users in AWS IAM Identity Center, secure the sign-in process in that service and turn
on MFA. For external user identities in your applications, you can use Amazon Cognito user pools
and secure the sign-in process in that service or through one of the supported identity providers in
Amazon Cognito user pools.
Additionally, for users in AWS IAM Identity Center, you can use AWS Verified Access to provide
an additional layer of security by verifying the user's identity and device posture before they are
granted access to AWS resources.
If you are using AWS Identity and Access Management (IAM) users, secure the sign-in process using
