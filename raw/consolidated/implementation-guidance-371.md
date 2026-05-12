---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 295
---

# Implementation guidance

Use temporary security credentials instead of long-term credentials for all AWS API and CLI
requests. API and CLI requests to AWS services must, in nearly every case, be signed using AWS
access keys. These requests can be signed with either temporary or long-term credentials. The
only time you should use long-term credentials, also known as long-term access keys, is if you are
using an IAM user or the AWS account root user. When you federate to AWS or assume an IAM
role through other methods, temporary credentials are generated. Even when you access the AWS
Management Console using sign-in credentials, temporary credentials are generated for you to
make calls to AWS services. There are few situations where you need long-term credentials and you
can accomplish nearly all tasks using temporary credentials.
Avoiding the use of long-term credentials in favor of temporary credentials should go hand in hand
with a strategy of reducing the usage of IAM users in favor of federation and IAM roles. While IAM
users have been used for both human and machine identities in the past, we now recommend not
using them to avoid the risks in using long-term access keys.
