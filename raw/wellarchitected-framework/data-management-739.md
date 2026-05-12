---
title: "Data management 739"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 744
---

# Data management 739

| Type | AWS Services | Key characteristics |
| --- | --- | --- |
| In-memory database | Amazon ElastiCache ,
Amazon MemoryDB for Redis | Used for applications that
require real-time access to
data, lowest latency and
highest throughput. You may
use in-memory databases for
application caching, session
management, gaming
leaderboards, low latency
ML feature store, microserv
ices messaging system, and a
high-throughput streaming
mechanism |
| Graph database | Amazon Neptune | Used for applications that
must navigate and query
millions of relationships
between highly connected
graph datasets with milliseco
nd latency at large scale.
Many companies use
graph databases for fraud
detection, social networkin
g, and recommendation
engines. |
| Time Series database | Amazon Timestream | Used to efficiently collect,
synthesize, and derive
insights from data that
changes over time. IoT
applications, DevOps, and
industrial telemetry can
utilize time-series databases. |
