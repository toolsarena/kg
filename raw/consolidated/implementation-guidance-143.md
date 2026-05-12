---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 541
---

# Implementation guidance

Services should be designed to process a known capacity of requests; this capacity can be
established through load testing. If request arrival rates exceed limits, the appropriate response
signals that a request has been throttled. This allows the consumer to handle the error and retry
later.
When your service requires a throttling implementation, consider implementing the token bucket
algorithm, where a token counts for a request. Tokens are refilled at a throttle rate per second and
emptied asynchronously by one token per request.
