---
title: "Best practices"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 493
---

# Best practices

• REL02-BP01 Use highly available network connectivity for your workload public endpoints
• REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-
premises environments
• REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability
• REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh
• REL02-BP05 Enforce non-overlapping private IP address ranges in all private address spaces
where they are connected
REL02-BP01 Use highly available network connectivity for your workload public endpoints
Building highly available network connectivity to public endpoints of your workloads can help
you reduce downtime due to loss of connectivity and improve the availability and SLA of your
workload. To achieve this, use highly available DNS, content delivery networks (CDNs), API
gateways, load balancing, or reverse proxies.


# Best practices

• REL03-BP01 Choose how to segment your workload
• REL03-BP02 Build services focused on specific business domains and functionality
• REL03-BP03 Provide service contracts per API

# Best practices

• REL04-BP01 Identify the kind of distributed systems you depend on
• REL04-BP02 Implement loosely coupled dependencies
• REL04-BP03 Do constant work
• REL04-BP04 Make mutating operations idempotent