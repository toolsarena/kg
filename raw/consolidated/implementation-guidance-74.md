---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 299
---

# Implementation guidance

In the past, credentials used to authenticate to databases, third-party APIs, tokens, and other
secrets might have been embedded in source code or in environment files. AWS provides several
mechanisms to store these credentials securely, automatically rotate them, and audit their usage.
The best way to approach secrets management is to follow the guidance of remove, replace, and
rotate. The most secure credential is one that you do not have to store, manage, or handle. There
might be credentials that are no longer necessary to the functioning of the workload that can be
safely removed.
For credentials that are still required for the proper functioning of the workload, there might be
an opportunity to replace a long-term credential with a temporary or short-term credential. For
example, instead of hard-coding an AWS secret access key, consider replacing that long-term
credential with a temporary credential using IAM roles.
