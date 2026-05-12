---
title: "SEC01-BP06 Automate deployment of standard security controls"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 281
---

# SEC01-BP06 Automate deployment of standard security controls

Apply modern DevOps practices as you develop and deploy security controls that are standard
across your AWS environments. Define standard security controls and configurations using
Infrastructure as Code (IaC) templates, capture changes in a version control system, test changes as
part of a CI/CD pipeline, and automate the deployment of changes to your AWS environments.
Desired outcome: IaC templates capture standardized security controls and commit them
to a version control system. CI/CD pipelines are in places that detect changes and automate
testing and deploying your AWS environments. Guardrails are in place to detect and alert on
misconfigurations in templates before proceeding to deployment. Workloads are deployed into
environments where standard controls are in place. Teams have access to deploy approved service
configurations through a self-service mechanism. Secure backup and recovery strategies are in
place for control configurations, scripts, and related data.
