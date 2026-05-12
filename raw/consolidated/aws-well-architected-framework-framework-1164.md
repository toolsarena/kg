---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 542
---

# AWS Well-Architected Framework Framework

The token bucket algorithm.
Amazon API Gateway implements the token bucket algorithm according to account and region
limits and can be configured per-client with usage plans. Additionally, Amazon Simple Queue
Service (Amazon SQS) and Amazon Kinesis can buffer requests to smooth out the request rate, and
allow higher throttling rates for requests that can be addressed. Finally, you can implement rate
limiting with AWS WAF to throttle specific API consumers that generate unusually high load.
