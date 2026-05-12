---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 345
---

# Implementation steps

1. Use cross-account roles to provide access to external accounts. Cross-account roles reduce
the amount of sensitive information that is stored by external accounts and third parties for
servicing their customers. Cross-account roles allow you to grant access to AWS resources
in your account securely to a third party, such as AWS Partners or other accounts in your
organization, while maintaining the ability to manage and audit that access. The third party
might be providing service to you from a hybrid infrastructure or alternatively pulling data
into an offsite location. IAM Roles Anywhere helps you allow third-party workloads to securely
interact with your AWS workloads and further reduce the need for long-term credentials.
You should not use long-term credentials or access keys associated with users to provide
external account access. Instead, use cross-account roles to provide the cross-account access.
2. Perform due diligence and ensure secure access for third-party SaaS providers. When
sharing resources with third-party SaaS providers, perform thorough due diligence to ensure
they have a secure and responsible approach to accessing your AWS resources. Evaluate their
shared responsibility model to understand what security measures they provide and what falls
under your responsibility. Ensure that the SaaS provider has a secure and auditable process for
accessing your resources, including the use of external IDs and least privilege access principles.
The use of external IDs helps address the confused deputy problem.
Implement security controls to ensure secure access and adherence to the principle of least
privilege when granting access to third-party SaaS providers. This may include the use of
external IDs, universally unique identifiers (UUIDs), and IAM trust policies that limit access to
only what is strictly necessary. Work closely with the SaaS provider to establish secure access
mechanisms, regularly review their access to your AWS resources, and conduct audits to ensure
compliance with your security requirements.
3. Deprecate customer-provided long-term credentials. Deprecate the use of long-term
credentials and use cross-account roles or IAM Roles Anywhere. If you must use long-term
credentials, establish a plan to migrate to role-based access. For details on managing keys, see
Identity management. Also, work with your AWS account team and the third party to establish a
