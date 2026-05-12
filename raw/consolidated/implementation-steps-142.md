---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 687
---

# Implementation steps

1. Determine a DR strategy that will satisfy recovery requirements for this workload.
Choosing a DR strategy is a trade-off between reducing downtime and data loss (RTO and RPO)
and the cost and complexity of implementing the strategy. You should avoid implementing a
strategy that is more stringent than it needs to be, as this incurs unnecessary costs.
For example, in the following diagram, the business has determined their maximum permissible
RTO as well as the limit of what they can spend on their service restoration strategy. Given the
business’ objectives, the DR strategies pilot light or warm standby will satisfy both the RTO and
the cost criteria.
