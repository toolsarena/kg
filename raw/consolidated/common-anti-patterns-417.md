---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 760
---

# Common anti-patterns:

• You cache data that changes frequently.
• You rely on cached data as if it is durably stored and always available.
• You don't consider the consistency of your cached data.
• You don't monitor the efficiency of your caching implementation.
Benefits of establishing this best practice: Storing data in a cache can improve read latency, read
throughput, user experience, and overall efficiency, as well as reduce costs.
Level of risk exposed if this best practice is not established: Medium
