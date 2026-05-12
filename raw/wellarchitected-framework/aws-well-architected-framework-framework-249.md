---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 333
---

# AWS Well-Architected Framework Framework

purpose, which you can apply to either an OU or an account. SCPs can enforce common access
controls, such as restricting access to specific AWS Regions, help prevent resources from being
deleted, or disabling potentially risky service actions. SCPs that you apply to the root of your
organization only affect its member accounts, not the management account. SCPs only govern the
principals within your organization. Your SCPs don't govern principals outside your organization
that are accessing your resources.
If you are using AWS Control Tower, you can leverage its controls and landing zones as the
foundation for your permission guardrails and multi-account environment. The landing zones
provide a pre-configured, secure baseline environment with separate accounts for different
workloads and applications. The guardrails enforce mandatory controls around security,
operations, and compliance through a combination of Service Control Policies (SCPs), AWS Config
rules, and other configurations. However, when using Control Tower guardrails and landing zones
alongside custom Organization SCPs, it's crucial to follow the best practices outlined in the AWS
documentation to avoid conflicts and ensure proper governance. Refer to the AWS Control Tower
guidance for AWS Organizations for detailed recommendations on managing SCPs, accounts, and
organizational units (OUs) within a Control Tower environment.
By adhering to these guidelines, you can effectively leverage Control Tower's guardrails, landing
zones, and custom SCPs while mitigating potential conflicts and ensuring proper governance and
control over your multi-account AWS environment.
A further step is to use IAM resource policies to scope the available actions that you can take on
the resources they govern, along with any conditions that the acting principal must meet. This
can be as broad as allowing all actions so long as the principal is part of your organization (using
the PrincipalOrgId condition key), or as granular as only allowing specific actions by a specific IAM
role. You can take a similar approach with conditions in IAM role trust policies. If a resource or role
trust policy explicitly names a principal in the same account as the role or resource it governs, that
principal does not need an attached IAM policy that grants the same permissions. If the principal is
in a different account from the resource, then the principal does need an attached IAM policy that
grants those permissions.
Often, a workload team will want to manage the permissions their workload requires. This may
require them to create new IAM roles and permission policies. You can capture the maximum scope
of permissions the team is allowed to grant in an IAM permission boundary, and associate this
document to an IAM role the team can then use to manage their IAM roles and permissions. This
approach can provide them the flexibility to complete their work while mitigating risks of having
IAM administrative access.
