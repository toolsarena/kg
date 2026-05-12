---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 779
---

# Common anti-patterns:

• You use TCP for all workloads regardless of performance requirements.
Benefits of establishing this best practice: Verifying that an appropriate protocol is used for
communication between users and workload components helps improve overall user experience
for your applications. For instance, connection-less UDP allows for high speed, but it doesn't offer
retransmission or high reliability. TCP is a full featured protocol, but it requires greater overhead
for processing the packets.
Level of risk exposed if this best practice is not established: Medium
