---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 542
---

# Implementation steps

You can configure API Gateway with throttling limits for your APIs and return 429 Too Many
Requests errors when limits are exceeded. You can use AWS WAF with your AWS AppSync and
API Gateway endpoints to enable rate limiting on a per IP address basis. Additionally, where your
system can tolerate asynchronous processing, you can put messages into a queue or stream to
speed up responses to service clients, which allows you to burst to higher throttle rates.
With asynchronous processing, when you’ve configured Amazon SQS as an event source for AWS
Lambda, you can configure maximum concurrency to avoid high event rates from consuming
available account concurrent execution quota needed for other services in your workload or
account.
While API Gateway provides a managed implementation of the token bucket, in cases where
you cannot use API Gateway, you can take advantage of language specific open-source
implementations (see related examples in Resources) of the token bucket for your services.
• Understand and configure API Gateway throttling limits at the account level per region, API per
stage, and API key per usage plan levels.
