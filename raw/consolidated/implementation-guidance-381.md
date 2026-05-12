---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 336
---

# Implementation guidance

Carefully manage and adjust access privileges that you grant to identities (such as users, roles,
groups) throughout their lifecycle. This lifecycle includes the initial onboarding phase, ongoing
changes in roles and responsibilities, and eventual offboarding or termination. Proactively manage
access based on the stage of the lifecycle to maintain the appropriate access level. Adhere to the
principle of least privilege to reduce the risk of excessive or unnecessary access Privileges.
You can manage the lifecycle of IAM users directly within the AWS account, or through federation
from your workforce identity provider to AWS IAM Identity Center. For IAM users, you can create,
modify, and delete users and their associated permissions within the AWS account. For federated
users, you can use IAM Identity Center to manage their lifecycle by synchronizing user and group
information from your organization's identity provider using the System for Cross-domain Identity
Management (SCIM) protocol.
SCIM is an open standard protocol for automated provisioning and deprovisioning of user identities
across different systems. By integrating your identity provider with IAM Identity Center using SCIM,
you can automatically synchronize user and group information, helping to validate that access
privileges are granted, modified, or revoked based on changes in your organization's authoritative
identity source.
As the roles and responsibilities of employees change within your organization, adjust their access
privileges accordingly. You can use IAM Identity Center's permission sets to define different job
roles or responsibilities and associate them with the appropriate IAM policies and permissions.
When an employee's role changes, you can update their assigned permission set to reflect their
new responsibilities. Verify that they have the necessary access while adhering to the principle of
least privilege.
