---
title: "REL07-BP01 Use automation when obtaining or scaling resources"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 581
---

# REL07-BP01 Use automation when obtaining or scaling resources

A cornerstone of reliability in the cloud is the programmatic definition, provisioning, and
management of your infrastructure and resources. Automation helps you streamline resource
provisioning, facilitate consistent and secure deployments, and scale resources across your entire
infrastructure.
Desired outcome: You manage your infrastructure as code (IaC). You define and maintain your
infrastructure code in version control systems (VCS). You delegate provisioning AWS resources
to automated mechanisms and leverage managed services like Application Load Balancer (ALB),
Network Load Balancer (NLB), and Auto Scaling groups. You provision your resources using
continuous integration/continuous delivery (CI/CD) pipelines so that code changes automatically
initiate resource updates, including updates to your Auto Scaling configurations.
