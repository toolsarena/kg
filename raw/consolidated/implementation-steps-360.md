---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 549
---

# Implementation steps

• Implement programmatic assertions or specific metrics in your software and use them to
explicitly alert on system issues. Amazon CloudWatch helps you create metrics and alarms based
on application log pattern and SDK instrumentation.
• Use CloudWatch metrics and alarms to fail away from impaired resources that are adding latency
to processing or repeatedly failing to process requests.
• Use asynchronous processing by designing APIs to accept requests and append requests to
internal queues using Amazon SQS and then respond to the message-producing client with a
success message so the client can release resources and move on with other work while backend
queue consumers process requests.
• Measure and monitor for queue processing latency by producing a CloudWatch metric each time
you take a message off a queue by comparing now to message timestamp.
• When failures prevent successful message processing or traffic spikes in volumes that cannot be
processed within service level agreements, sideline older or excess traffic to a spillover queue.
This allows priority processing of new work, and older work when capacity is available. This
technique is an approximation of LIFO processing and allows normal system processing for all
new work.
• Use dead letter or redrive queues to move messages that can’t be processed out of the backlog
into a location that can be researched and resolved later
• Either retry or, when tolerable, drop old messages by comparing now to the message timestamp
and discarding messages that are no longer relevant to the requesting client.


# Implementation steps

• Configure timeouts on remote service calls and take advantage of built-in language timeout
features or open source timeout libraries.
• When your workload makes calls with an AWS SDK, review the documentation for language
specific timeout configuration.
• Python