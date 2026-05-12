---
title: "Best practices 24"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 29
---

# Best practices 24

| SEC 2: How do you manage identities for people and machines? |
| --- |
| There are two types of identities you need to manage when approaching operating secure AWS
workloads. Understanding the type of identity you need to manage and grant access helps you
verify the right identities have access to the right resources under the right conditions.
Human Identities: Your administrators, developers, operators, and end users require an identity
to access your AWS environments and applications. These are members of your organization, or
external users with whom you collaborate, and who interact with your AWS resources via a web
browser, client application, or interactive command line tools.
Machine Identities: Your service applications, operational tools, and workloads require an
identity to make requests to AWS services, for example, to read data. These identities include
machines running in your AWS environment such as Amazon EC2 instances or AWS Lambda
functions. You may also manage machine identities for external parties who need access.
Additionally, you may also have machines outside of AWS that need access to your AWS
environment. |

| SEC 3: How do you manage permissions for people and machines? |
| --- |
| Manage permissions to control access to people and machine identities that require access to
AWS and your workload. Permissions control who can access what, and under what conditions. |
