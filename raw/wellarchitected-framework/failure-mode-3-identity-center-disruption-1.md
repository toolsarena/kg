---
title: "Failure Mode 3: Identity Center disruption"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 327
---

# Failure Mode 3: Identity Center disruption

In the unlikely event of an IAM Identity Center or AWS Region disruption, we recommend that
you set up a configuration that you can use to provide temporary access to the AWS Management
Console.
The emergency access process uses direct federation from your identity provider to IAM in an
emergency account. For detail on the process and design considerations, see Set up emergency
access to the AWS Management Console.
