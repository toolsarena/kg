---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 523
---

# AWS Well-Architected Framework Framework

and receiving messages through a message broker. Event streaming allows your workload and
its dependency to use a streaming service to publish and subscribe to events, delivered as
continuous streams of data, that need to be processed as soon as possible.
• Messaging and event streaming handle messages differently so you need to make trade-off
decisions based on:
• Message priority: message brokers can process high-priority messages ahead of normal
messages. In event streaming, all messages have the same priority.
• Message consumption: message brokers ensure that consumers receive the message. Event
streaming consumers must keep track of the last message they have read.
• Message ordering: with messaging, receiving messages in the exact order they are sent is
not guaranteed unless you use a first-in-first-out (FIFO) approach. Event streaming always
preserves the order in which the data was produced.
• Message deletion: with messaging, the consumer must delete the message after processing
it. The event streaming service appends the message to a stream and remains in there until
the message's retention period expires. This deletion policy makes event streaming suitable for
replaying messages.
• Define how your workload knows when its dependency completes its work. For instance, when
your workload invokes a Lambda function asynchronously, Lambda places the event in a queue
and returns a success response without additional information. After processing is complete, the
Lambda function can send the result to a destination, configurable based on success or failure.
• Build your workload to handle duplicate messages by leveraging idempotency. Idempotency
means that the results of your workload do not change even if your workload is generated
more than once for the same message. It is important to point out that messaging or streaming
services will redeliver a message if a network failure occurs or if an acknowledgement has not
been received.
• If your workload does not get a response from its dependency, it needs to resubmit the request.
Consider limiting the number of retries to preserve your workload's CPU, memory, and network
resources to handle other requests. The AWS Lambda documentation shows how to handle
errors for asynchronous invocation.
• Leverage suitable observability, debugging, and tracing tools to manage and operate your
workload's asynchronous communication with its dependency. You can use Amazon CloudWatch
to monitor messaging and event streaming services. You can also instrument your workload with
AWS X-Ray to quickly gain insights for troubleshooting problems.
