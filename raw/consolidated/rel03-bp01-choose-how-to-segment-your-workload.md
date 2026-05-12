---
title: "REL03-BP01 Choose how to segment your workload"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 510
---

# REL03-BP01 Choose how to segment your workload

Workload segmentation is important when determining the resilience requirements of your
application. Monolithic architecture should be avoided whenever possible. Instead, carefully
consider which application components can be broken out into microservices. Depending on your
application requirements, this may end up being a combination of a service-oriented architecture
(SOA) with microservices where possible. Workloads that are capable of statelessness are more
capable of being deployed as microservices.
Desired outcome: Workloads should be supportable, scalable, and as loosely coupled as possible.
When making choices about how to segment your workload, balance the benefits against the
complexities. What is right for a new product racing to first launch is different than what a
workload built to scale from the start needs. When refactoring an existing monolith, you will
need to consider how well the application will support a decomposition towards statelessness.
Breaking services into smaller pieces allows small, well-defined teams to develop and manage
them. However, smaller services can introduce complexities which include possible increased
latency, more complex debugging, and increased operational burden.
