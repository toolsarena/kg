---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 761
---

# AWS Well-Architected Framework Framework

itself), resulting in the lowest possible latency. Clients can also continue to serve some queries
when the backend datastore is unavailable, increasing the availability of the overall system.
One disadvantage of this approach is that when multiple clients are involved, they may store the
same cached data locally. This results in both duplicate storage usage and data inconsistency
between those clients. One client might cache the results of a query, and one minute later another
client can run the same query and get a different result.
