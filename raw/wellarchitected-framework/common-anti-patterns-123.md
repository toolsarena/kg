---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 502
---

# Common anti-patterns:

• Failing to consider future growth, resulting in CIDR blocks that are too small and requiring
reconfiguration, potentially causing downtime.
• Incorrectly estimating how many IP addresses an elastic load balancer can use.
• Deploying many high traffic load balancers into the same subnets
• Using automated scaling mechanisms whilst failing to monitor IP address consumption.
• Defining excessively large CIDR ranges well beyond future growth expectations, which can lead
to difficulty peering with other networks with overlapping address ranges.
Benefits of establishing this best practice: This ensures that you can accommodate the growth of
your workloads and continue to provide availability as you scale up.
Level of risk exposed if this best practice is not established: Medium
