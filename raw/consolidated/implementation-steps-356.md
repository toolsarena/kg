---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 528
---

# Implementation steps

• Components in an event-driven architecture are initiated by events. Events are actions that
happen in a system, such as a user adding an item to a cart. When an action is successful, an
event is generated that actuates the next component of the system.
• Building Event-driven Applications with Amazon EventBridge
• AWS re:Invent 2022 - Designing Event-Driven Integrations using Amazon EventBridge
• Distributed messaging systems have three main parts that need to be implemented for a queue
based architecture. They include components of the distributed system, the queue that is used
for decoupling (distributed on Amazon SQS servers), and the messages in the queue. A typical
system has producers which initiate the message into the queue, and the consumer which
receives the message from the queue. The queue stores messages across multiple Amazon SQS
servers for redundancy.
• Basic Amazon SQS architecture
• Send Messages Between Distributed Applications with Amazon Simple Queue Service
• Microservices, when well-utilized, enhance maintainability and boost scalability, as loosely
coupled components are managed by independent teams. It also allows for the isolation of
behaviors to a single component in case of changes.
