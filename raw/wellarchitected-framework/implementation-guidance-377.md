---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 319
---

# Implementation guidance

The principle of least privilege states that identities should only be permitted to perform the
smallest set of actions necessary to fulfill a specific task. This balances usability, efficiency, and
security. Operating under this principle helps limit unintended access and helps track who has
access to what resources. IAM users and roles have no permissions by default. The root user has full
access by default and should be tightly controlled, monitored, and used only for tasks that require
root access.
IAM policies are used to explicitly grant permissions to IAM roles or specific resources. For example,
identity-based policies can be attached to IAM groups, while S3 buckets can be controlled by
resource-based policies.
When you create an IAM policy, you can specify the service actions, resources, and conditions that
must be true for AWS to allow or deny access. AWS supports a variety of conditions to help you
scope down access. For example, by using the PrincipalOrgID condition key, you can deny actions if
the requestor isn't a part of your AWS Organization.
You can also control requests that AWS services make on your behalf, such as AWS CloudFormation
creating an AWS Lambda function, using the CalledVia condition key. You can layer different policy
types to establish defense-in-depth and limit the overall permissions of your users. You can also
restrict what permissions can be granted and under what conditions. For example, you can allow
your workload teams to create their own IAM policies for systems they build, but only if they apply
a Permission Boundary to limit the maximum permissions they can grant.
