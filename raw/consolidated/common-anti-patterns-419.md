---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 775
---

# Common anti-patterns:

• You don’t consider your workload requirements when choosing the load balancer type.
• You don’t leverage the load balancer features for performance optimization.
• The workload is exposed directly to the internet without a load balancer.
• You route all internet traffic through existing load balancers.
• You use generic TCP load balancing and making each compute node handle SSL encryption.
Benefits of establishing this best practice: A load balancer handles the varying load of your
application traffic in a single Availability Zone or across multiple Availability Zones and enables
high availability, automatic scaling, and better utilization for your workload.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• Setting up too many non-critical alerts, leading to alert fatigue.
• Not prioritizing alerts based on KPIs, making it hard to understand the business impact of issues.
• Neglecting to address root causes, leading to repetitive alerts for the same issue.