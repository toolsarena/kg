---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 546
---

# Implementation steps

• Determine the optimal layer in your application stack to implement retries for the services your
application relies on.
• Be aware of existing SDKs that implement proven retry strategies with exponential backoff and
jitter for your language of choice, and favor these over writing your own retry implementations.
• Verify that services are idempotent before implementing retries. Once retries are implemented,
be sure they are both tested and regularly exercise in production.
• When calling AWS service APIs, use the AWS SDKs and AWS CLI and understand the retry
configuration options. Determine if the defaults work for your use case, test, and adjust as
needed.
