---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 272
---

# AWS Well-Architected Framework Framework

a. Eliminate any long-lived programmatic credentials (access and secret keys) for the root user.
b. If root user access keys already exist, you should transition processes using those keys to use
temporary access keys from an AWS Identity and Access Management (IAM) role, then delete
the root user access keys.
3. Determine if you need to store credentials for the root user.
a. If you are using AWS Organizations to create new member accounts, the initial password for
the root user on new member accounts is set to a random value that is not exposed to you.
Consider using the password reset flow from your AWS Organization management account to
gain access to the member account if needed.
b. For standalone AWS accounts or the management AWS Organization account, consider
creating and securely storing credentials for the root user. Use MFA for the root user.
4. Use preventative controls for member account root users in AWS multi-account environments.
a. Consider using the Disallow Creation of Root Access Keys for the Root User preventative
guard rail for member accounts.
b. Consider using the Disallow Actions as a Root User preventative guard rail for member
accounts.
