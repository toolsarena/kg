---
title: "COST07-BP04 Implement pricing models for all components of this workload"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 902
---

# COST07-BP04 Implement pricing models for all components of this workload

Permanently running resources should utilize reserved capacity such as Savings Plans or Reserved
Instances. Short-term capacity is configured to use Spot Instances, or Spot Fleet. On-Demand
Instances are only used for short-term workloads that cannot be interrupted and do not run long
enough for reserved capacity, between 25% to 75% of the period, depending on the resource type.
Level of risk exposed if this best practice is not established: Low
