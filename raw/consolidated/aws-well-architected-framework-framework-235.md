---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 315
---

# AWS Well-Architected Framework Framework

privilege access model is a recommended approach. AWS Managed policies provide predefined IAM
policies that cover most common use cases.
AWS services, such as AWS Secrets Manager and AWS Systems Manager Parameter Store, can help
decouple secrets from the application or workload securely. In Secrets Manager, you can establish
automatic rotation for your credentials. You can use Systems Manager to reference parameters in
your scripts, commands, SSM documents, configuration, and automation workflows by using the
unique name that you specified when you created the parameter.
You can use AWS IAM Roles Anywhere to obtain temporary security credentials in IAM for
workloads that run outside of AWS. Your workloads can use the same IAM policies and IAM roles
that you use with AWS applications to access AWS resources.
Where possible, prefer short-term temporary credentials over long-term static credentials. For
scenarios in which you need users with programmatic access and long-term credentials, use access
key last used information to rotate and remove access keys.
Users need programmatic access if they want to interact with AWS outside of the AWS
Management Console. The way to grant programmatic access depends on the type of user that's
accessing AWS.
To grant users programmatic access, choose one of the following options.


# AWS Well-Architected Framework Framework

• Identify, arrange, and manage secrets easily using enhanced search in AWS Secrets Manager