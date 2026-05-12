---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 527
---

# AWS Well-Architected Framework Framework

EventBridge, which can abstract clients (event producers) from the services they rely on (event
consumers). Amazon Simple Notification Service (Amazon SNS) is an effective solution when you
need high-throughput, push-based, many-to-many messaging. Using Amazon SNS topics, your
publisher systems can fan out messages to a large number of subscriber endpoints for parallel
processing.
While queues offer several advantages, in most hard real-time systems, requests older than a
threshold time (often seconds) should be considered stale (the client has given up and is no longer
waiting for a response), and not processed. This way more recent (and likely still valid requests) can
be processed instead.
Desired outcome: Implementing loosely coupled dependencies allows you to minimize the surface
area for failure to a component level, which helps diagnose and resolve issues. It also simplifies
development cycles, allowing teams to implement changes at a modular level without affecting
the performance of other components that depend on it. This approach provides the capability
to scale out at a component level based on resource needs, as well as utilization of a component
contributing to cost-effectiveness.
