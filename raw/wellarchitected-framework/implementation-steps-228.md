---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 949
---

# Implementation steps

• Analyze the client requests to determine how to respond to them. Questions to consider include:
• Can this request be processed asynchronously?
• Does the client have retry capability?
• If the client has retry capability, then you can implement throttling, which tells the source that if
it cannot service the request at the current time, it should try again later.
• You can use Amazon API Gateway to implement throttling.
• For clients that cannot perform retries, a buffer needs to be implemented to flatten the demand
curve. A buffer defers request processing, allowing applications that run at different rates to
communicate effectively. A buffer-based approach uses a queue or a stream to accept messages
from producers. Messages are read by consumers and processed, allowing the messages to run at
the rate that meets the consumers’ business requirements.
• Amazon Simple Queue Service (Amazon SQS) is a managed service that provides queues that
allow a single consumer to read individual messages.
• Amazon Kinesis provides a stream that allows many consumers to read the same messages.
• Analyze the overall demand, rate of change, and required response time to right size the throttle
or buffer required.
