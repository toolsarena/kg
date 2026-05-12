---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 532
---

# Implementation guidance

In a distributed system, performing an action at most once (the client makes only one request) or
at least once (the client keeps requesting until success is confirmed) is relatively straightforward.
However, it's challenging to implement exactly once behavior. To achieve this, your clients should
generate and provide an idempotency token for each request.
