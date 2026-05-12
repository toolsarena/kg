---
title: "For third-party identities:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 296
---

# For third-party identities:

• When granting third parties, such as software as a service (SaaS) providers, access to resources in
your AWS account, you can use cross-account roles and resource-based policies. Additionally, you
can use the Amazon Cognito OAuth 2.0 grant client credentials flow for B2B SaaS customers or
partners.
User identities that access your AWS resources through web browsers, client applications, mobile
apps, or interactive command-line tools:
• If you need to grant applications for consumers or customers access to your AWS resources, you
can use Amazon Cognito identity pools or Amazon Cognito user pools to provide temporary
credentials. The permissions for the credentials are configured through IAM roles. You can also
define a separate IAM role with limited permissions for guest users who are not authenticated.
