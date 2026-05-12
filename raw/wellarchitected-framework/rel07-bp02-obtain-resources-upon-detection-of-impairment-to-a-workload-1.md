---
title: "REL07-BP02 Obtain resources upon detection of impairment to a workload"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 584
---

# REL07-BP02 Obtain resources upon detection of impairment to a workload

Scale resources reactively when necessary if availability is impacted, to restore workload
availability.
You first must configure health checks and the criteria on these checks to indicate when availability
is impacted by lack of resources. Then, either notify the appropriate personnel to manually scale
the resource, or start automation to automatically scale it.
Scale can be manually adjusted for your workload (for example, changing the number of EC2
instances in an Auto Scaling group, or modifying throughput of a DynamoDB table through the
AWS Management Console or AWS CLI). However, automation should be used whenever possible
(refer to Use automation when obtaining or scaling resources).
Desired outcome: Scaling activities (either automatically or manually) are initiated to restore
availability upon detection of a failure or degraded customer experience.
Level of risk exposed if this best practice is not established: Medium
