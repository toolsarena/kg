---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 271
---

# AWS Well-Architected Framework Framework

AWS root user to perform tasks that specifically require it. The root user login credentials must be
closely guarded, and multi-factor authentication (MFA) should always be used for the AWS account
root user.
In addition to the normal authentication flow to log into your root user using a username,
password, and multi-factor authentication (MFA) device, there are account recovery flows to log
into your AWS account root user given access to the email address and phone number associated
with your account. Therefore, it is equally important to secure the root user email account where
the recovery email is sent and the phone number associated with the account. Also consider
potential circular dependencies where the email address associated with the root user is hosted on
email servers or domain name service (DNS) resources from the same AWS account.
When using AWS Organizations, there are multiple AWS accounts each of which have a root user.
One account is designated as the management account and several layers of member accounts
can then be added underneath the management account. Prioritize securing your management
account’s root user, then address your member account root users. The strategy for securing your
management account’s root user can differ from your member account root users, and you can
place preventative security controls on your member account root users.
