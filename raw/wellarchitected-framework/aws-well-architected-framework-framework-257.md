---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 342
---

# AWS Well-Architected Framework Framework

policies to each OU to help you meet your budgetary, security, and compliance needs. You can
also control how AWS artificial intelligence (AI) and machine learning (ML) services can collect
and store data, and use the multi-account management of the AWS services integrated with
Organizations.
2. Integrate AWS Organizations with AWS services: When you use an AWS service to perform
tasks on your behalf in the member accounts of your organization, AWS Organizations creates
an IAM service-linked role (SLR) for that service in each member account. You should manage
trusted access using the AWS Management Console, the AWS APIs, or the AWS CLI. For
prescriptive guidance on turning on trusted access, see Using AWS Organizations with other AWS
services and AWS services that you can use with Organizations.
3. Establish a data perimeter: A data perimeter provides a clear boundary of trust and ownership.
On AWS, it is typically represented as your AWS organization managed by AWS Organizations,
along with any on-premises networks or systems that access your AWS resources. The goal of
the data perimeter is to verify that access is allowed if the identity is trusted, the resource is
trusted, and the network is expected. However, establishing a data perimeter is not a one-size-
fits-all approach. Evaluate and adopt the control objectives outlined in the Building a Perimeter
on AWS whitepaper based on your specific security risk models and requirements. You should
carefully consider your unique risk posture and implement the perimeter controls that align with
your security needs.
4. Use resource sharing in AWS services and restrict accordingly: Many AWS services allow
you to share resources with another account, or target a resource in another account, such as
Amazon Machine Images (AMIs) and AWS Resource Access Manager (AWS RAM). Restrict the
ModifyImageAttribute API to specify the trusted accounts to share the AMI with. Specify
the ram:RequestedAllowsExternalPrincipals condition when using AWS RAM to
constrain sharing to your organization only, to help prevent access from untrusted identities. For
prescriptive guidance and considerations, see Resource sharing and external targets.
5. Use AWS RAM to share securely in an account or with other AWS accounts: AWS RAM helps
you securely share the resources that you have created with roles and users in your account
and with other AWS accounts. In a multi-account environment, AWS RAM allows you to create
a resource once and share it with other accounts. This approach helps reduce your operational
overhead while providing consistency, visibility, and auditability through integrations with
Amazon CloudWatch and AWS CloudTrail, which you do not receive when using cross-account
access.
