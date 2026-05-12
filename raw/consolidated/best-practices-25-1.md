---
title: "Best practices 25"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 30
---

# Best practices 25

| Which user needs
programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use
console credentials as
temporary credentials to sign
programmatic requests to the
AWS CLI, AWS SDKs, or AWS
APIs. | Following the instructions for
the interface that you want to
use.
• For the AWS CLI, see Login
for AWS local development
in the AWS Command Line
Interface User Guide.
• For AWS SDKs, see Login
for AWS local development
in the AWS SDKs and Tools
Reference Guide. |
| Workforce identity
(Users managed in IAM
Identity Center) | Use temporary credentials to
sign programmatic requests
to the AWS CLI, AWS SDKs, or
AWS APIs. | Following the instructions for
the interface that you want to
use.
• For the AWS CLI, see
Configuring the AWS
CLI to use AWS IAM
Identity Center in the AWS
Command Line Interface
User Guide.
• For AWS SDKs, tools, and
AWS APIs, see IAM Identity
Center authentication in
the AWS SDKs and Tools
Reference Guide. |
| IAM | Use temporary credentials to
sign programmatic requests
to the AWS CLI, AWS SDKs, or
AWS APIs. | Following the instructions in
Using temporary credentia
ls with AWS resources in the
IAM User Guide. |
