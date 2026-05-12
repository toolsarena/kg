---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 775
---

# Implementation guidance

Load balancers act as the entry point for your workload, from which point they distribute the
traffic to your backend targets, such as compute instances or containers, to improve utilization.
Choosing the right load balancer type is the first step to optimize your architecture. Start by listing
your workload characteristics, such as protocol (like TCP, HTTP, TLS, or WebSockets), target type
(like instances, containers, or serverless), application requirements (like long running connections,
user authentication, or stickiness), and placement (like Region, Local Zone, Outpost, or zonal
isolation).
AWS provides multiple models for your applications to use load balancing. Application Load
Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced
request routing targeted at the delivery of modern application architectures, including
microservices and containers.
