---
title: "Common steps for all failure modes"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 327
---

# Common steps for all failure modes

• Create an AWS account dedicated to emergency access processes. Pre-create the IAM resources
needed in the account such as IAM roles or IAM users, and optionally IAM Identity Providers.
Additionally, pre-create cross-account IAM roles in the workload AWS accounts with trust
relationships with corresponding IAM roles in the emergency access account. You can use
CloudFormation StackSets with AWS Organizations to create such resources in the member
accounts in your organization.
• Create AWS Organizations service control policies (SCPs) to deny the deletion and modification
of the cross-account IAM roles in the member AWS accounts.
• Enable CloudTrail for the emergency access AWS account and send the trail events to a central
S3 bucket in your log collection AWS account. If you are using AWS Control Tower to set up and
govern your AWS multi-account environment, then every account you create using AWS Control
Tower or enroll in AWS Control Tower has CloudTrail enabled by default and sent to an S3 bucket
in a dedicated log archive AWS account.
