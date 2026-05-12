---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 977
---

# Common anti-patterns:

• You store all data in the same AWS Region independent of where the data users are.
• You do not optimize data size and format before moving it over the network.
Benefits of establishing this best practice: Optimizing data movement across the network reduces
the total networking resources required for the workload and lowers its environmental impact.
Level of risk exposed if this best practice is not established: Medium
