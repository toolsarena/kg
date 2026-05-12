---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 511
---

# AWS Well-Architected Framework Framework

to start with a monolith architecture, you must ensure that it’s modular and can ultimately
evolve to SOA or microservices as your product scales with user adoption. SOA and microservices
offer respectively smaller segmentation, which is preferred as a modern scalable and reliable
architecture, but there are trade-offs to consider, especially when deploying a microservice
architecture.
One primary trade-off is that you now have a distributed compute architecture that can make it
harder to achieve user latency requirements and there is additional complexity in the debugging
and tracing of user interactions. You can use AWS X-Ray to assist you in solving this problem.
Another effect to consider is increased operational complexity as you increase the number of
applications that you are managing, which requires the deployment of multiple independency
components.


# AWS Well-Architected Framework Framework

• Consider following the Strangler Fig pattern to refactor a monolith into smaller components.