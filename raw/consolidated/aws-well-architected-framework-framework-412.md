---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 543
---

# AWS Well-Architected Framework Framework

• Apply AWS WAF rate limiting rules to API Gateway and AWS AppSync endpoints to protect
against floods and block malicious IPs. Rate limiting rules can also be configured on AWS
AppSync API keys for A2A consumers.
• Consider whether you require more throttling control than rate limiting for AWS AppSync APIs,
and if so, configure an API Gateway in front of your AWS AppSync endpoint.
• When Amazon SQS queues are set up as triggers for Lambda queue consumers, set maximum
concurrency to a value that processes enough to meet your service level objectives but does
not consume concurrency limits impacting other Lambda functions. Consider setting reserved
concurrency on other Lambda functions in the same account and region when you consume
queues with Lambda.
• Use API Gateway with native service integrations to Amazon SQS or Kinesis to buffer requests.
• If you cannot use API Gateway, look at language specific libraries to implement the token bucket
algorithm for your workload. Check the examples section and do your own research to find a
suitable library.
• Test limits that you plan to set, or that you plan to allow to be increased, and document the
tested limits.
• Do not increase limits beyond what you establish in testing. When increasing a limit, verify that
provisioned resources are already equivalent to or greater than those in test scenarios before
applying the increase.


# AWS Well-Architected Framework Framework

• The three most important AWS WAF rate-based rules
• Java Bucket4j
• Python token-bucket
• Node token-bucket
• .NET System Threading Rate Limiting

# AWS Well-Architected Framework Framework

when calling services that are idempotent and where retries improve your client availability. Decide
what the timeouts are and when to stop retrying based on your use case. Build and exercise testing
scenarios for those retry use cases.

# AWS Well-Architected Framework Framework

• Resilience4j Retry