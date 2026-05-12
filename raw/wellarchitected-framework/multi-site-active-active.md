---
title: "Multi-site active/active"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 691
---

# Multi-site active/active

You can run your workload simultaneously in multiple Regions as part of a multi-site active/
active strategy. Multi-site active/active serves traffic from all regions to which it is deployed.
Customers may select this strategy for reasons other than DR. It can be used to increase
availability, or when deploying a workload to a global audience (to put the endpoint closer to
users and/or to deploy stacks localized to the audience in that region). As a DR strategy, if the
workload cannot be supported in one of the AWS Regions to which it is deployed, then that
Region is evacuated, and the remaining Regions are used to maintain availability. Multi-site
active/active is the most operationally complex of the DR strategies, and should only be selected
when business requirements necessitate it.
