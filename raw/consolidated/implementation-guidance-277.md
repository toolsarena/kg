---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 954
---

# Implementation guidance

Unused or underutilized components in a cloud workload consume unnecessary compute, storage
or network resources. Remove or refactor these components to directly reduce waste and improve
the overall efficiency of a cloud workload. This is an iterative improvement process which can be
initiated by changes in demand or the release of a new cloud service. For example, a significant
drop in AWS Lambda function run time can be indicate a need to lower the memory size. Also, as
AWS releases new services and features, the optimal services and architecture for your workload
may change.
Continually monitor workload activity and look for opportunities to improve the utilization level
of individual components. By removing idle components and performing rightsizing activities, you
meet your business requirements with the fewest cloud resources.
