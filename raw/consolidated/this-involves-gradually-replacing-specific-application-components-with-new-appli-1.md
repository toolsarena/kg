---
title: "This involves gradually replacing specific application components with new applications"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 512
---

# This involves gradually replacing specific application components with new applications

and services. AWS Migration Hub Refactor Spaces acts as the starting point for incremental
refactoring. For more details, see Seamlessly migrate on-premises legacy workloads using a
strangler pattern.
• Implementing microservices may require a service discovery mechanism to allow these
distributed services to communicate with each other. AWS App Mesh can be used with service-
oriented architectures to provide reliable discovery and access of services. AWS Cloud Map can
also be used for dynamic, DNS-based service discovery.
• If you’re migrating from a monolith to SOA, Amazon MQ can help bridge the gap as a service bus
when redesigning legacy applications in the cloud.
• For existing monoliths with a single, shared database, choose how to reorganize the data into
smaller segments. This could be by business unit, access pattern, or data structure. At this point
in the refactoring process, you should choose to move forward with a relational or non-relational
(NoSQL) type of database. For more details, see From SQL to NoSQL.
