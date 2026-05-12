---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 761
---

# Implementation steps

• Identify databases, APIs and network services that could benefit from caching. Services that have
heavy read workloads, have a high read-to-write ratio, or are expensive to scale are candidates
for caching.
• Database Caching
• Enabling API caching to enhance responsiveness
• Identify the appropriate type of caching strategy that best fits your access pattern.
• Caching strategies
• AWS Caching Solutions
• Follow Caching Best Practices for your data store.
• Configure a cache invalidation strategy, such as a time-to-live (TTL), for all data that balances
freshness of data and reducing pressure on backend datastore.
• Enable features such as automatic connection retries, exponential backoff, client-side timeouts,
and connection pooling in the client, if available, as they can improve performance and
reliability.
• Best practices: Redis clients and Amazon ElastiCache (Redis OSS)
