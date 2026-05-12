---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 553
---

# AWS Well-Architected Framework Framework

• When using AWS SDKs or AWS CLI commands in your workload, configure default timeout
values by setting the AWS configuration defaults for connectTimeoutInMillis and
tlsNegotiationTimeoutInMillis.
• Apply command line options cli-connect-timeout and cli-read-timeout to control one-
off AWS CLI commands to AWS services.
• Monitor remote service calls for timeouts, and set alarms on persistent errors so that you can
proactively handle error scenarios.
• Implement CloudWatch Metrics and CloudWatch anomaly detection on call error rates, service
level objectives for latency, and latency outliers to provide insight into managing overly
aggressive or permissive timeouts.
• Configure timeouts on Lambda functions.
• API Gateway clients must implement their own retries when handling timeouts. API Gateway
supports a 50 millisecond to 29 second integration timeout for downstream integrations and
does not retry when integration requests timeout.
• Implement the circuit breaker pattern to avoid making remote calls when they are timing out.
Open the circuit to avoid failing calls and close the circuit when calls are responding normally.
• For container based workloads, review App Mesh Envoy features to leverage built in timeouts
and circuit breakers.
• Use AWS Step Functions to build low code circuit breakers for remote service calls, especially
where calling AWS native SDKs and supported Step Functions integrations to simplify your
workload.
