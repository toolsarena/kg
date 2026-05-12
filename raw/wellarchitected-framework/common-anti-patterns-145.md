---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 590
---

# Common anti-patterns:

• Performing load testing on deployments that are not the same configuration as your production.
• Performing load testing only on individual pieces of your workload, and not on the entire
workload.
• Performing load testing with a subset of requests and not a representative set of actual requests.
• Performing load testing to a small safety factor above expected load.
Benefits of establishing this best practice: You know what components in your architecture fail
under load and be able to identify what metrics to watch to indicate that you are approaching that
load in time to address the problem, preventing the impact of that failure.
Level of risk exposed if this best practice is not established: Medium
