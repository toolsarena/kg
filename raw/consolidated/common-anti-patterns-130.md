---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 527
---

# Common anti-patterns:

• Deploying a monolithic workload.
• Directly invoking APIs between workload tiers with no capability of failover or asynchronous
processing of the request.
• Tight coupling using shared data. Loosely coupled systems should avoid sharing data through
shared databases or other forms of tightly coupled data storage, which can reintroduce tight
coupling and hinder scalability.
• Ignoring back pressure. Your workload should have the ability to slow down or stop incoming
data when a component can't process it at the same rate.
Benefits of establishing this best practice: Loose coupling helps isolate behavior of a component
from other components that depend on it, increasing resiliency and agility. Failure in one
component is isolated from others.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• You apply idempotency indiscriminately, even when not needed.
• You introduce overly complex logic for implementing idempotency.