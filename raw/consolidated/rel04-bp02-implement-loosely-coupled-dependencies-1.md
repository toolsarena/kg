---
title: "REL04-BP02 Implement loosely coupled dependencies"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 525
---

# REL04-BP02 Implement loosely coupled dependencies

Dependencies such as queuing systems, streaming systems, workflows, and load balancers are
loosely coupled. Loose coupling helps isolate behavior of a component from other components
that depend on it, increasing resiliency and agility.
Decoupling dependencies, such as queuing systems, streaming systems, and workflows, help
minimize the impact of changes or failure on a system. This separation isolates a component's
behavior from affecting others that depend on it, improving resilience and agility.
In tightly coupled systems, changes to one component can necessitate changes in other
components that rely on it, resulting in degraded performance across all components. Loose
