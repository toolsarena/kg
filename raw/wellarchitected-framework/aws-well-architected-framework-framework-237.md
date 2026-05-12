---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 320
---

# AWS Well-Architected Framework Framework

as billing, database administrators, and data scientists. These policies can help narrow the access
that users have while you determine how to implement the least privilege policies.
• Remove unnecessary permissions: Detect and remove unused IAM entities, credentials, and
permissions to achieve the principle of least privilege. You can use IAM Access Analyzer to
identify external and unused access, and IAM Access Analyzer policy generation can help fine-
tune permissions policies.
• Ensure that users have limited access to production environments: Users should only have
access to production environments with a valid use case. After the user performs the specific
tasks that required production access, access should be revoked. Limiting access to production
environments helps prevent unintended production-impacting events and lowers the scope of
impact of unintended access.
• Consider permissions boundaries: A permissions boundary is a feature for using a managed
policy that sets the maximum permissions that an identity-based policy can grant to an IAM
entity. An entity's permissions boundary allows it to perform only the actions that are allowed by
both its identity-based policies and its permissions boundaries.
• Refine access using attribute-based access control and resource tags Attribute-based access
control (ABAC) using resource tags can be used to refine permissions when supported. You can
use an ABAC model that compares principal tags to resource tags to refine access based on
custom dimensions you define. This approach can simplify and reduce the number of permission
policies in your organization.
• It is recommended that ABAC only be used for access control when both the principals and
resources are owned by your AWS Organization. External parties may use the same tag names
and values as your organization for their own principals and resources. If you rely solely on
these name-value pairs for granting access to external party principals or resources, you may
provide unintended permissions.
• Use service control policies for AWS Organizations: Service control policies centrally control
the maximum available permissions for member accounts in your organization. Importantly,
you can use service control policies to restrict root user permissions in member accounts. Also
consider using AWS Control Tower, which provides prescriptive managed controls that enrich
AWS Organizations. You can also define your own controls within Control Tower.
• Establish a user lifecycle policy for your organization: User lifecycle policies define tasks to
perform when users are onboarded onto AWS, change job role or scope, or no longer need
access to AWS. Perform permission reviews during each step of a user's lifecycle to verify that
permissions are properly restrictive and to avoid permissions creep.
