---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 305
---

# Implementation guidance

Guidance for workforce users accessing AWS Workforce users like employees and contractors
in your organization may require access to AWS using the AWS Management Console or AWS
Command Line Interface (AWS CLI) to perform their job functions. You can grant AWS access
to your workforce users by federating from your centralized identity provider to AWS at two
levels: direct federation to each AWS account or federating to multiple accounts in your AWS
organization.
To federate your workforce users directly with each AWS account, you can use a centralized identity
provider to federate to AWS Identity and Access Management in that account. The flexibility of
IAM allows you to enable a separate SAML 2.0 or an Open ID Connect (OIDC) Identity Provider for
each AWS account and use federated user attributes for access control. Your workforce users will
use their web browser to sign in to the identity provider by providing their credentials (such as
passwords and MFA token codes). The identity provider issues a SAML assertion to their browser
that is submitted to the AWS Management Console sign in URL to allow the user to single sign-on
to the AWS Management Console by assuming an IAM Role. Your users can also obtain temporary
AWS API credentials for use in the AWS CLI or AWS SDKs from AWS STS by assuming the IAM role
using a SAML assertion from the identity provider.
To federate your workforce users with multiple accounts in your AWS organization, you can use
AWS IAM Identity Center to centrally manage access for your workforce users to AWS accounts and
applications. You enable Identity Center for your organization and configure your identity source.
IAM Identity Center provides a default identity source directory which you can use to manage
your users and groups. Alternatively, you can choose an external identity source by connecting to
your external identity provider using SAML 2.0 and automatically provisioning users and groups
using SCIM, or connecting to your Microsoft AD Directory using Directory Service. Once an identity
source is configured, you can assign access to users and groups to AWS accounts by defining least-
privilege policies in your permission sets. Your workforce users can authenticate through your
central identity provider to sign in to the AWS access portal and single-sign on to the AWS accounts
and cloud applications assigned to them. Your users can configure the AWS CLI v2 to authenticate
with Identity Center and get credentials to run AWS CLI commands. Identity Center also allows
