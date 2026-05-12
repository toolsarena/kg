---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 971
---

# Common anti-patterns:

• You procure large block storage or file system for future need.
• You overprovision the input and output operations per second (IOPS) of your file system.
• You do not monitor the utilization of your data volumes.
Benefits of establishing this best practice: Minimizing over-provisioning for storage system
reduces the idle resources and improves the overall efficiency of your workload.
Level of risk exposed if this best practice is not established: Medium


# Common anti-patterns:

• You duplicate data that can be easily obtained or recreated.