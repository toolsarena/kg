---
title: "Some other options for scenarios requiring long-term credentials include:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 297
---

# Some other options for scenarios requiring long-term credentials include:

• Build your own token vending API (using Amazon API Gateway).
• For scenarios where you must use long-term credentials or credentials other than AWS access
keys (such as database logins), you can use a service designed to handle the management of
secrets, such as AWS Secrets Manager. Secrets Manager simplifies the management, rotation,
and secure storage of encrypted secrets. Many AWS services support a direct integration with
Secrets Manager.
• For multi-cloud integrations, you can use identity federation based on your source credential
service provider (CSP) credentials (see AWS STS AssumeRoleWithWebIdentity).
For more information about rotating long-term credentials, see rotating access keys.
