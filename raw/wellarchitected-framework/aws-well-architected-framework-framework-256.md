---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 341
---

# AWS Well-Architected Framework Framework

access continuously, and be alerted on inappropriate or unexpected sharing. Review Analyze
public and cross-account access to help you establish governance to reduce the external access
to only resources that require it, and to establish a process to monitor continuously and alert
automatically.
Cross-account sharing within AWS Organizations is supported by a number of AWS services, such
as AWS Security Hub CSPM, Amazon GuardDuty, and AWS Backup. These services allow for data to
be shared to a central account, be accessible from a central account, or manage resources and data
from a central account. For example, AWS Security Hub CSPM can transfer findings from individual
accounts to a central account where you can view all the findings. AWS Backup can take a backup
for a resource and share it across accounts. You can use AWS Resource Access Manager (AWS RAM)
to share other common resources, such as VPC subnets and Transit Gateway attachments, AWS
Network Firewall, or Amazon SageMaker AI pipelines.
To restrict your account to only share resources within your organization, use service control
policies (SCPs) to prevent access to external principals. When sharing resources, combine identity-
based controls and network controls to create a data perimeter for your organization to help
protect against unintended access. A data perimeter is a set of preventive guardrails to help verify
that only your trusted identities are accessing trusted resources from expected networks. These
controls place appropriate limits on what resources can be shared and prevent sharing or exposing
resources that should not be allowed. For example, as a part of your data perimeter, you can use
VPC endpoint policies and the AWS:PrincipalOrgId condition to ensure the identities accessing
your Amazon S3 buckets belong to your organization. It is important to note that SCPs do not
apply to service-linked roles or AWS service principals.
When using Amazon S3, turn off ACLs for your Amazon S3 bucket and use IAM policies to define
access control. For restricting access to an Amazon S3 origin from Amazon CloudFront, migrate
from origin access identity (OAI) to origin access control (OAC) which supports additional features
including server-side encryption with AWS Key Management Service.
In some cases, you might want to allow sharing resources outside of your organization or grant a
third party access to your resources. For prescriptive guidance on managing permissions to share
resources externally, see Permissions management.
