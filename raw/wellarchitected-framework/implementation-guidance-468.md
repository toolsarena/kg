---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 629
---

# Implementation guidance

On a ship, bulkheads ensure that a hull breach is contained within one section of the hull. In
complex systems, this pattern is often replicated to allow fault isolation. Fault isolated boundaries
restrict the effect of a failure within a workload to a limited number of components. Components
outside of the boundary are unaffected by the failure. Using multiple fault isolated boundaries,
you can limit the impact on your workload. On AWS, customers can use multiple Availability Zones
and Regions to provide fault isolation, but the concept of fault isolation can be extended to your
workload’s architecture as well.
The overall workload is partitioned cells by a partition key. This key needs to align with the grain of
the service, or the natural way that a service's workload can be subdivided with minimal cross-cell
interactions. Examples of partition keys are customer ID, resource ID, or any other parameter easily
accessible in most API calls. A cell routing layer distributes requests to individual cells based on the
partition key and presents a single endpoint to clients.
