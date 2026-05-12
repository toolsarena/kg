---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 325
---

# AWS Well-Architected Framework Framework

• Test emergency access processes periodically to verify that the steps are clear and grant the
correct level of access quickly and efficiently. Your emergency access processes should be tested
as part of incident response simulations (SEC10-BP07) and disaster recovery tests (REL13-BP03).
Failure Mode 1: Identity provider used to federate to AWS is unavailable
As described in SEC02-BP04 Rely on a centralized identity provider, we recommend relying on a
centralized identity provider to federate your workforce users to grant access to AWS accounts. You
can federate to multiple AWS accounts in your AWS organization using IAM Identity Center, or you
can federate to individual AWS accounts using IAM. In both cases, workforce users authenticate
with your centralized identity provider before being redirected to an AWS sign-in endpoint to
single sign-on.
In the unlikely event that your centralized identity provider is unavailable, your workforce users
can't federate to AWS accounts or manage their workloads. In this emergency event, you can
provide an emergency access process for a small set of administrators to access AWS accounts to
perform critical tasks that cannot wait until your centralized identity providers are back online.
For example, your identity provider is unavailable for 4 hours and during that period you need
to modify the upper limits of an Amazon EC2 Auto Scaling group in a Production account to
handle an unexpected spike in customer traffic. Your emergency administrators should follow the
emergency access process to gain access to the specific production AWS account and make the
necessary changes.
The emergency access process relies on a pre-created emergency access AWS account that is used
solely for emergency access and has AWS resources (such as IAM roles and IAM users) to support
the emergency access process. During normal operations, no one should access the emergency
access account and you must monitor and alert on the misuse of this account (for more detail, see
the preceding Common guidance section).
The emergency access account has emergency access IAM roles with permissions to assume cross-
account roles in the AWS accounts that require emergency access. These IAM roles are pre-created
and configured with trust policies that trust the emergency account's IAM roles.
The emergency access process can use one of the following approaches:
• You can pre-create a set of IAM users for your emergency administrators in the emergency access
account with associated strong passwords and MFA tokens. These IAM users have permissions to
assume the IAM roles that then allow cross-account access to the AWS account where emergency
access is required. We recommend creating as few such users as possible and assigning each
