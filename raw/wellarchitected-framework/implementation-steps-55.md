---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 309
---

# Implementation steps

• Regularly audit credentials: Auditing the identities that are configured in your identity provider
and IAM helps verify that only authorized identities have access to your workload. Such identities
can include, but are not limited to, IAM users, AWS IAM Identity Center users, Active Directory
users, or users in a different upstream identity provider. For example, remove people that leave
the organization, and remove cross-account roles that are no longer required. Have a process
in place to periodically audit permissions to the services accessed by an IAM entity. This helps
you identify the policies you need to modify to remove any unused permissions. Use credential
reports and AWS Identity and Access Management Access Analyzer to audit IAM credentials and
permissions. You can use Amazon CloudWatch to set up alarms for specific API calls called within
your AWS environment. Amazon GuardDuty can also alert you to unexpected activity, which
might indicate overly permissive access or unintended access to IAM credentials.
• Rotate credentials regularly: When you are unable to use temporary credentials, rotate long-
term IAM access keys regularly (maximum every 90 days). If an access key is unintentionally
disclosed without your knowledge, this limits how long the credentials can be used to access
your resources. For information about rotating access keys for IAM users, see Rotating access
keys.
• Review IAM permissions: To improve the security of your AWS account, regularly review and
monitor each of your IAM policies. Verify that policies adhere to the principle of least privilege.
• Consider automating IAM resource creation and updates: IAM Identity Center automates many
IAM tasks, such as role and policy management. Alternatively, AWS CloudFormation can be used
to automate the deployment of IAM resources, including roles and policies, to reduce the chance
of human error because the templates can be verified and version controlled.
• Use IAM Roles Anywhere to replace IAM users for machine identities: IAM Roles Anywhere
allows you to use roles in areas that you traditionally could not, such as on-premise servers. IAM
Roles Anywhere uses a trusted X.509 certificate to authenticate to AWS and receive temporary
credentials. Using IAM Roles Anywhere avoids the need to rotate these credentials, as long-term
credentials are no longer stored in your on-premises environment. Please note that you will need
to monitor and rotate the X.509 certificate as it approaches expiration.
