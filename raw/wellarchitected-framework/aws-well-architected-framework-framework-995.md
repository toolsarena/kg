---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 326
---

# AWS Well-Architected Framework Framework

user to a single emergency administrator. During an emergency, an emergency administrator
user signs into the emergency access account using their password and MFA token code,
switches to the emergency access IAM role in the emergency account, and finally switches to the
emergency access IAM role in the workload account to perform the emergency change action.
The advantage of this approach is that each IAM user is assigned to one emergency administrator
and you can know which user signed-in by reviewing CloudTrail events. The disadvantage is that
you have to maintain multiple IAM users with their associated long-lived passwords and MFA
tokens.
• You can use the emergency access AWS account root user to sign into the emergency access
account, assume the IAM role for emergency access, and assume the cross-account role in the
workload account. We recommend setting a strong password and multiple MFA tokens for the
root user. We also recommend storing the password and the MFA tokens in a secure enterprise
credential vault that enforces strong authentication and authorization. You should secure
the password and MFA token reset factors: set the email address for the account to an email
distribution list that is monitored by your cloud security administrators, and the phone number
of the account to a shared phone number that is also monitored by security administrators.
The advantage of this approach is that there is one set of root user credentials to manage. The
disadvantage is that since this is a shared user, multiple administrators have ability to sign in as
the root user. You must audit your enterprise vault log events to identify which administrator
checked out the root user password.
Failure Mode 2: Identity provider configuration on AWS is modified or has expired
To allow your workforce users to federate to AWS accounts, you can configure the IAM Identity
Center with an external identity provider or create an IAM Identity Provider (SEC02-BP04).
Typically, you configure these by importing a SAML meta-data XML document provided by your
identity provider. The meta-data XML document includes a X.509 certificate corresponding to a
private key that the identity provider uses to sign its SAML assertions.
These configurations on the AWS-side may be modified or deleted by mistake by an administrator.
In another scenario, the X.509 certificate imported into AWS may expire and a new meta-data XML
with a new certificate has not yet been imported into AWS. Both scenarios can break federation to
AWS for your workforce users, resulting in an emergency.
In such an emergency event, you can provide your identity administrators access to AWS to fix the
federation issues. For example, your identity administrator uses the emergency access process to
sign into the emergency access AWS account, switches to a role in the Identity Center administrator
