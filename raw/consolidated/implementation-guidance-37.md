---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 189
---

# Implementation guidance

An ORR is two things: a process and a checklist. Your ORR process should be adopted by your
organization and supported by an executive sponsor. At a minimum, ORRs must be conducted
before a workload launches to general availability. Run the ORR throughout the software
development lifecycle to keep it up to date with best practices or new requirements. The ORR
checklist should include configuration items, security and governance requirements, and best
practices from your organization. Over time, you can use services, such as AWS Config, AWS
Security Hub CSPM, and AWS Control Tower Guardrails, to build best practices from the ORR into
guardrails for automatic detection of best practices.


# Implementation guidance

There are several ways for human identities to sign in to AWS. It is an AWS best practice to rely on
a centralized identity provider using federation (direct SAML 2.0 federation between AWS IAM and