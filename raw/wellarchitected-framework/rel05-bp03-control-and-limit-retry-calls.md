---
title: "REL05-BP03 Control and limit retry calls"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 544
---

# REL05-BP03 Control and limit retry calls

Use exponential backoff to retry requests at progressively longer intervals between each retry.
Introduce jitter between retries to randomize retry intervals. Limit the maximum number of retries.
Desired outcome: Typical components in a distributed software system include servers, load
balancers, databases, and DNS servers. During normal operation, these components can respond
to requests with errors that are temporary or limited, and also errors that would be persistent
regardless of retries. When clients make requests to services, the requests consume resources
including memory, threads, connections, ports, or any other limited resources. Controlling and
limiting retries is a strategy to release and minimize consumption of resources so that system
components under strain are not overwhelmed.
When client requests time out or receive error responses, they should determine whether or not
to retry. If they do retry, they do so with exponential backoff with jitter and a maximum retry
value. As a result, backend services and processes are given relief from load and time to self-heal,
resulting in faster recovery and successful request servicing.
