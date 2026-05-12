---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 917
---

# AWS Well-Architected Framework Framework

Demand curve with two distinct peaks that require high provisioned capacity
Assume a workload with the demand curve shown in preceding image. This workload has two
peaks, and to handle those peaks, the resource capacity as shown by orange line is provisioned.
The resources and energy used for this workload are not indicated by the area under the demand
curve, but the area under the provisioned capacity line, as provisioned capacity is needed to handle
those two peaks. Flattening the workload demand curve can help you to reduce the provisioned
capacity for a workload and reduce its environmental impact. To smooth out the peak, consider to
implement throttling or buffering solution.
To understand them better, let’s explore throttling and buffering.
Throttling: If the source of the demand has retry capability, then you can implement throttling.
Throttling tells the source that if it cannot service the request at the current time, it should try
again later. The source waits for a period of time, and then retries the request. Implementing
throttling has the advantage of limiting the maximum amount of resources and costs of the
workload. In AWS, you can use Amazon API Gateway to implement throttling.
Buffer based: A buffer-based approach uses producers (components that send messages to the
queue), consumers (components that receive messages from the queue), and a queue (which holds
messages) to store the messages. Messages are read by consumers and processed, allowing the
messages to run at the rate that meets the consumers’ business requirements. By using a buffer-
centric methodology, messages from producers are housed in queues or streams, ready to be
accessed by consumers at a pace that aligns with their operational demands.
In AWS, you can choose from multiple services to implement a buffering approach. Amazon
Simple Queue Service(Amazon SQS) is a managed service that provides queues that allow a
single consumer to read individual messages. Amazon Kinesis provides a stream that allows many
consumers to read the same messages.
