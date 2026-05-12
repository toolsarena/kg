---
title: "Synchronous dependency"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 522
---

# Synchronous dependency

In synchronous communications, your workload sends a request to its dependency and blocks
the operation waiting for a response. When its dependency receives the request, it tries to handle
it as soon as possible and sends a response back to your workload. A significant challenge with
synchronous communication is that it causes temporal coupling, which requires your workload and
its dependencies to be available at the same time. When your workload needs to communicate
synchronously with its dependencies, consider the following guidance:
• Your workload should not rely on multiple synchronous dependencies to perform a single
function. This chain of dependencies increases overall brittleness because all dependencies in the
pathway need to be available in order for the request to complete successfully.
• When a dependency is unhealthy or unavailable, determine your error handling and retry
strategies. Avoid using bimodal behavior. Bimodal behavior is when your workload exhibits
different behavior under normal and failure modes. For more details on bimodal behavior, see
REL11-BP05 Use static stability to prevent bimodal behavior.
• Keep in mind that failing fast is better than making your workload wait. For instance, the AWS
Lambda Developer Guide describes how to handle retries and failures when you invoke Lambda
functions.
• Set timeouts when your workload calls its dependency. This technique avoids waiting too long or
waiting indefinitely for a response. For helpful discussion of this issue, see Tuning AWS Java SDK
HTTP request settings for latency-aware Amazon DynamoDB applications.
• Minimize the number of calls made from your workload to its dependency to fulfill a single
request. Having chatty calls between them increases coupling and latency.
