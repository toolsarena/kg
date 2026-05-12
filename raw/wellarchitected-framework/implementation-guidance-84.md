---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 338
---

# Implementation guidance

If your account is in AWS Organizations, you can grant access to resources to the entire
organization, specific organizational units, or individual accounts. If your account is not a member
of an organization, you can share resources with individual accounts. You can grant direct cross-
account access using resource-based policies — for example, Amazon Simple Storage Service
(Amazon S3) bucket policies — or by allowing a principal in another account to assume an IAM
role in your account. When using resource policies, verify that access is only granted to authorized
principals. Define a process to approve all resources which are required to be publicly available.
AWS Identity and Access Management Access Analyzer uses provable security to identify all access
paths to a resource from outside of its account. It reviews resource policies continuously, and
reports findings of public and cross-account access to make it simple for you to analyze potentially
broad access. Consider configuring IAM Access Analyzer with AWS Organizations to verify that you
have visibility to all your accounts. IAM Access Analyzer also allows you to preview findings before
deploying resource permissions. This allows you to validate that your policy changes grant only
the intended public and cross-account access to your resources. When designing for multi-account
access, you can use trust policies to control in what cases a role can be assumed. For example, you
could use the PrincipalOrgId condition key to deny an attempt to assume a role from outside
your AWS Organizations.
AWS Config can report resources that are misconfigured, and through AWS Config policy checks,
can detect resources that have public access configured. Services such as AWS Control Tower
and AWS Security Hub CSPM simplify deploying detective controls and guardrails across AWS
Organizations to identify and remediate publicly exposed resources. For example, AWS Control
Tower has a managed guardrail which can detect if any Amazon EBS snapshots are restorable by
AWS accounts.
