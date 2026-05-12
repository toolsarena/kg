---
title: "Remote caching"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 761
---

# Remote caching

To solve the issue of duplicate data between clients, a fast external service, or remote cache, can
be used to store the queried data. Instead of checking a local data store, each client will check the
remote cache before querying the backend datastore. This strategy allows for more consistent
responses between clients, better efficiency in stored data, and a higher volume of cached data
because the storage space scales independently of clients.
The disadvantage of a remote cache is that the overall system may see a higher latency, as an
additional network hop is required to check the remote cache. Client-side caching can be used
alongside remote caching for multi-level caching to improve the latency.


# Resources

Refer to the following resources to learn more about our best practices for Security.

# Resources

Refer to the following resources to learn more about our best practices for Cost Optimization.

# Resources

Refer to the following resources to learn more about our best practices for sustainability.

# Resources

Refer to the following resources to learn more about our best practices for Reliability.

# Resources 20

| OPS 11: How do you evolve operations? |
| --- |
| Dedicate time and resources for nearly continuous incremental improvement to evolve the
effectiveness and efficiency of your operations. |

# Resources 20

| OPS 11: How do you evolve operations? |
| --- |
| Dedicate time and resources for nearly continuous incremental improvement to evolve the
effectiveness and efficiency of your operations. |

# Resources

Refer to the following resources to learn more about our best practices for Performance Efficiency.