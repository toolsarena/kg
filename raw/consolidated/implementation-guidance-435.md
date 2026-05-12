---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 517
---

# Implementation guidance

Once you have identified business domains and determined your workload segmentation, you
can develop your service APIs. First, define machine-readable service contracts for APIs, and then
implement an API versioning strategy. When you are ready to integrate services over common
protocols like REST, GraphQL, or asynchronous events, you can incorporate AWS services into your
architecture to integrate your components with strongly-typed API contracts.


# Implementation guidance

The following sections contain both general and specific implementation guidance for each kind of
dependency.

# Implementation guidance

Implement loosely coupled dependencies. There are various solutions that allow you to build
loosely coupled applications. These include services for implementing fully managed queues,