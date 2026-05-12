---
title: "Identity and access management 295"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 300
---

# Identity and access management 295

| Credential type | Description | Suggested strategy |
| --- | --- | --- |
| IAM access keys | AWS IAM access and secret
keys used to assume IAM
roles inside of a workload | Replace: Use IAM roles
assigned to the compute
instances (such as Amazon
EC2 or AWS Lambda) instead.
For interoperability with third
parties that require access
to resources in your AWS
account, ask if they support
AWS cross-account access.
For mobile apps, consider
using temporary credentia
ls through Amazon Cognito
identity pools (federated
identities). For workloads
running outside of AWS,
consider IAM Roles Anywhere
or AWS Systems Manager
Hybrid Activations. For
containers see Amazon ECS
task IAM role or Amazon EKS
node IAM role. |
| SSH keys | Secure Shell private keys
used to log into Linux EC2
instances, manually or as part
of an automated process | Replace: Use AWS Systems
Manager or EC2 Instance
Connect to provide
programmatic and human
access to EC2 instances using
IAM roles. |
