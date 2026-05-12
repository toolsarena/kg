---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 526
---

# AWS Well-Architected Framework Framework

coupling breaks this dependency so that dependent components only need to know the versioned
and published interface. Implementing loose coupling between dependencies isolates a failure in
one from impacting another.
Loose coupling allows you to modify code or add features to a component while minimizing risk
to other components that depend on it. It also allows for granular resilience at a component level
where you can scale out or even change underlying implementation of the dependency.
To further improve resiliency through loose coupling, make component interactions asynchronous
where possible. This model is suitable for any interaction that does not need an immediate
response and where an acknowledgment that a request has been registered will suffice. It involves
one component that generates events and another that consumes them. The two components
do not integrate through direct point-to-point interaction but usually through an intermediate
durable storage layer, such as an Amazon SQS queue, a streaming data platform such as Amazon
Kinesis, or AWS Step Functions.
Figure 4: Dependencies such as queuing systems and load balancers are loosely coupled
Amazon SQS queues and AWS Step Functions are just two ways to add an intermediate layer
for loose coupling. Event-driven architectures can also be built in the AWS Cloud using Amazon
