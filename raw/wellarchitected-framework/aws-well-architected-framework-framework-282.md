---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 373
---

# AWS Well-Architected Framework Framework

AWS CloudFormation or another infrastructure as code (IaC) tool of your choice, commit them
to a version control system, and deploy them using CI/CD pipelines. Use this approach to gain
the traditional benefits of DevOps for managing your network controls, such as more predictable
releases, automated testing using tools like AWS CloudFormation Guard, and detecting drift
between your deployed environment and your desired configuration.
Based on the decisions you made as part of SEC05-BP01 Create network layers, you may have
a central management approach to creating VPCs that are dedicated for ingress, egress, and
inspection flows. As described in the AWS Security Reference Architecture (AWS SRA), you can
define these VPCs in a dedicated Network infrastructure account. You can use similar techniques
to centrally define the VPCs used by your workloads in other accounts, their security groups, AWS
Network Firewall deployments, Route 53 Resolver rules and DNS Firewall configurations, and other
network resources. You can share these resources with your other accounts with the AWS Resource
Access Manager. With this approach, you can simplify the automated testing and deployment of
your network controls to the Network account, with only one destination to manage. You can do
this in a hybrid model, where you deploy and share certain controls centrally and delegate other
controls to the individual workload teams and their respective accounts.
