---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 302
---

# Implementation steps

1. Identify code paths containing hard-coded credentials using automated tools such as Amazon
CodeGuru.
a. Use Amazon CodeGuru to scan your code repositories. Once the review is complete, filter on
Type=Secrets in CodeGuru to find problematic lines of code.
2. Identify credentials that can be removed or replaced.
a. Identify credentials no longer needed and mark for removal.
b. For AWS Secret Keys that are embedded in source code, replace them with IAM roles
associated with the necessary resources. If part of your workload is outside AWS but requires
IAM credentials to access AWS resources, consider IAM Roles Anywhere or AWS Systems
Manager Hybrid Activations.
3. For other third-party, long-lived secrets that require the use of the rotate strategy, integrate
Secrets Manager into your code to retrieve third-party secrets at runtime.
a. The CodeGuru console can automatically create a secret in Secrets Manager using the
discovered credentials.
b. Integrate secret retrieval from Secrets Manager into your application code.
