---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 521
---

# Common anti-patterns:

• Workload waits indefinitely for a response from its dependencies, which could lead to workload
clients timing out, not knowing if their request has been received.
• Workload uses a chain of dependent systems that call each other synchronously. This requires
each system to be available and to successfully process a request before the whole chain can
succeed, leading to potentially brittle behavior and overall availability.
• Workload communicates with its dependencies asynchronously and rely on the concept of
exactly-once guaranteed delivery of messages, when often it is still possible to receive duplicate
messages.
• Workload does not use proper batch scheduling tools and allows concurrent execution of the
same batch job.
Benefits of establishing this best practice: It is common for a given workload to implement one
or more style of communication between synchronous, asynchronous, and batch. This best practice
helps you identify the different trade-offs associated with each style of communication to make
your workload able to tolerate disruptions in any of its dependencies.
Level of risk exposed if this best practice is not established: High
