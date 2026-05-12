---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 893
---

# AWS Well-Architected Framework Framework

Showback refers to reports that break down cloud costs into attributable categories, such as
consumers, business units, general ledger accounts, or other responsible entities. The goal of
showback is to show teams, business units, or individuals the cost of their consumed cloud
resources.
Chargeback means to allocate central service spend to cost units based on a strategy suitable for
a specific financial management process. For customers, chargeback charges the cost incurred
from one shared services account to different financial cost categories suitable for a customer
reporting process. By establishing chargeback mechanisms, you can report costs incurred by
different business units, products, and teams.
Workloads can be categorized as critical and non-critical. Based on this classification, use shared
resources with general configurations for less critical workloads. To further optimize costs, reserve
dedicated servers solely for critical workloads. Share resources or provision them across several
accounts to manage them efficiently. Even with distinct development, testing, and production
environments, secure sharing is feasible and does not compromise organizational structure.
To improve your understanding and optimize cost and usage for containerized applications, use
split cost allocation data which helps you allocate costs to individual business entities based on
how the application consumes shared compute and memory resources. Split cost allocation data
helps you achieve task-level showback and chargeback in container workloads running on Amazon
Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS).
For distributed architectures, build a shared services VPC, which provides centralized access to
shared services required by workloads in each of the VPCs. These shared services can include
resources such as directory services or VPC endpoints. To reduce administrative overhead and cost,
share resources from a central location instead of building them in each VPC.
When you use shared resources, you can save on operational costs, maximize resource utilization,
and improve consistency. In a multi-account design, you can host some AWS services centrally
and access them using several applications and accounts in a hub to save cost. You can use AWS
Resource Access Manager (AWS RAM) to share other common resources, such as VPC subnets and
AWS Transit Gateway attachments, AWS Network Firewall, or Amazon SageMaker AI pipelines.
In a multi-account environment, use AWS RAM to create a resource once and share it with other
accounts.
Organizations should tag shared costs effectively and verify that they do not have a significant
portion of their costs untagged or unallocated. If you do not allocate shared costs effectively
and no one takes accountability for shared costs management, shared cloud costs can spiral. You
