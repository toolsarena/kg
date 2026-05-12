---
title: "COST09-BP02 Implement a buffer or throttle to manage demand"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 916
---

# COST09-BP02 Implement a buffer or throttle to manage demand

Buffering and throttling modify the demand on your workload, smoothing out any peaks.
Implement throttling when your clients perform retries. Implement buffering to store the request
and defer processing until a later time. Verify that your throttles and buffers are designed so clients
receive a response in the required time.
Level of risk exposed if this best practice is not established: Medium
