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


# Implementation guidance

Implementing graceful degradation helps minimize the impact of dependency failures on
component function. Ideally, a component detects dependency failures and works around them in
a way that minimally impacts other components or customers.