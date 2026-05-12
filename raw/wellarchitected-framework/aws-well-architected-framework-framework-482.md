---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 631
---

# AWS Well-Architected Framework Framework

• Consequently, cross-cell interactions should be avoided or kept to a minimum, as those
interactions create dependencies between cells and therefore diminish the fault isolation
improvements.
3. Router layer: The router layer is a shared component between cells, and therefore cannot follow
the same compartmentalization strategy as with cells.
• It is recommended for the router layer to distribute requests to individual cells using a
partition mapping algorithm in a computationally efficient manner, such as combining
cryptographic hash functions and modular arithmetic to map partition keys to cells.
• To avoid multi-cell impacts, the routing layer must remain as simple and horizontally scalable
as possible, which necessitates avoiding complex business logic within this layer. This has the
added benefit of making it easy to understand its expected behavior at all times, allowing for
thorough testability. As explained by Colm MacCárthaigh in Reliability, constant work, and a
good cup of coffee, simple designs and constant work patterns produce reliable systems and
reduce anti-fragility.
4. Cell size: Cells should have a maximum size and should not be allowed to grow beyond it.
• The maximum size should be identified by performing thorough testing, until breaking points
are reached and safe operating margins are established. For more detail on how to implement
testing practices, see REL07-BP04 Load test your workload
• The overall workload should grow by adding additional cells, allowing the workload to scale
with increases in demand.
5. Multi-AZ or Multi-Region strategies: Multiple layers of resilience should be leveraged to protect
against different failure domains.
• For resilience, you should use an approach that builds layers of defense. One layer protects
against smaller, more common disruptions by building a highly available architecture using
multiple AZs. Another layer of defense is meant to protect against rare events like widespread
natural disasters and Region-level disruptions. This second layer involves architecting your
application to span multiple AWS Regions. Implementing a multi-Region strategy for your
workload helps protect it against widespread natural disasters that affect a large geographic
region of a country, or technical failures of Region-wide scope. Be aware that implementing
a multi-Region architecture can be significantly complex, and is usually not required for most
workloads. For more detail, see REL10-BP01 Deploy the workload to multiple locations.
6. Code deployment: A staggered code deployment strategy should be preferred over deploying
code changes to all cells at the same time.
