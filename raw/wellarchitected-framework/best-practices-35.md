---
title: "Best practices 35"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 40
---

# Best practices 35

| REL 2: How do you plan your network topology? |
| --- |
| Workloads often exist in multiple environments. These include multiple cloud environments
(both publicly accessible and private) and possibly your existing data center infrastructure. Plans
must include network considerations such as intra- and inter-system connectivity, public IP
address management, private IP address management, and domain name resolution. |

| REL 3: How do you design your workload service architecture? |
| --- |
| Build highly scalable and reliable workloads using a service-oriented architecture (SOA) or
a microservices architecture. Service-oriented architecture (SOA) is the practice of making
software components reusable via service interfaces. Microservices architecture goes further to
make components smaller and simpler. |

| REL 4: How do you design interactions in a distributed system to prevent failures? |
| --- |
| Distributed systems rely on communications networks to interconnect components, such as
servers or services. Your workload must operate reliably despite data loss or latency in these
networks. Components of the distributed system must operate in a way that does not negativel
y impact other components or the workload. These best practices prevent failures and improve
mean time between failures (MTBF). |
