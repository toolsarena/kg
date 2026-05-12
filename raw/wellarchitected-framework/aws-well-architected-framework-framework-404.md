---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 533
---

# AWS Well-Architected Framework Framework

By using idempotency tokens, a service can distinguish between new requests and repeated ones.
When a service receives a request with an idempotency token, it checks if the token has already
been used. If the token has been used, the service retrieves and returns the stored response. If
the token is new, the service processes the request, stores the response along with the token, and
then returns the response. This mechanism makes all responses idempotent, which enhances the
reliability and consistency of the distributed system.
Idempotency is also an important behavior of event-driven architectures. These architectures are
typically backed by a message queue such as Amazon SQS, Amazon MQ, Amazon Kinesis Streams,
or Amazon Managed Streaming for Apache Kafka (MSK). In some circumstances, a message
that was published only once may be accidentally delivered more than once. When a publisher
generates and includes idempotency tokens in messages, it requests that the processing of any
duplicate message received doesn't result in a repeated action for the same message. Consumers
should keep track of each token received and ignore messages that contain duplicate tokens.
Services and consumers should also pass the received idempotency token to any downstream
services that it calls. Every downstream service in the processing chain is similarly responsible for
making sure that idempotency is implemented to avoid the side effect of processing a message
more than once.
