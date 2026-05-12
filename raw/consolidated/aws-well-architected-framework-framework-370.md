---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 490
---

# AWS Well-Architected Framework Framework

• Not considering the potential of inaccessible resources in calculating total quota needed for each
Region.
• Not considering AWS service fault isolation boundaries for some services and their potential
abnormal usage patterns.
Benefits of establishing this best practice: When service disruption events impact application
availability, use the cloud to implement strategies to recover from these events. An example
strategy is creating additional resources to replace inaccessible resources to accommodate failover
conditions without exhausting your service limit.
Level of risk exposed if this best practice is not established: Medium
