---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 552
---

# AWS Well-Architected Framework Framework

Services should also protect themselves from abnormally expensive content with throttles and
server-side timeouts.
• Requests that take abnormally long due to a service impairment can be timed out and retried.
Consideration should be given to service costs for the request and retry, but if the cause is
a localized impairment, a retry is not likely to be expensive and will reduce client resource
consumption. The timeout may also release server resources depending on the nature of the
impairment.
• Requests that take a long time to complete because the request or response has failed to be
delivered by the network can be timed out and retried. Because the request or response was
not delivered, failure would have been the outcome regardless of the length of timeout. Timing
out in this case will not release server resources, but it will release client resources and improve
workload performance.
Take advantage of well-established design patterns like retries and circuit breakers to handle
timeouts gracefully and support fail-fast approaches. AWS SDKs and AWS CLI allow for
configuration of both connection and request timeouts and for retries with exponential backoff
and jitter. AWS Lambda functions support configuration of timeouts, and with AWS Step Functions,
you can build low code circuit breakers that take advantage of pre-built integrations with AWS
services and SDKs. AWS App Mesh Envoy provides timeout and circuit breaker capabilities.
