---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 306
---

# AWS Well-Architected Framework Framework

single-sign on access to AWS applications such as Amazon SageMaker AI Studio and AWS IoT
Sitewise Monitor portals.
After you follow the preceding guidance, your workforce users will no longer need to use IAM users
and groups for normal operations when managing workloads on AWS. Instead, your users and
groups are managed outside of AWS and users are able to access AWS resources as a federated
identity. Federated identities use the groups defined by your centralized identity provider. You
should identify and remove IAM groups, IAM users, and long-lived user credentials (passwords and
access keys) that are no longer needed in your AWS accounts. You can find unused credentials using
IAM credential reports, delete the corresponding IAM users and delete IAM groups. You can apply a
Service Control Policy (SCP) to your organization that helps prevent the creation of new IAM users
and groups, enforcing that access to AWS is via federated identities.
