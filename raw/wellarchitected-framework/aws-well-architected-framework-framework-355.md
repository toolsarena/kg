---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 473
---

# AWS Well-Architected Framework Framework

• Establish an automated and programmatic method to check if a service quota has been changed
in one region but not in other regions in the same account (see REL01-BP02 Manage service
quotas across accounts and regions and REL01-BP04 Monitor and manage quotas).
• Automate scanning application logs and metrics to determine if there are any quota or service
constraint errors. If these errors are present, send alerts to the monitoring system.
• Establish engineering procedures to calculate the required change in quota (see REL01-BP05
Automate quota management) once it has been identified that larger quotas are required for
specific services.
• Create a provisioning and approval workflow to request changes in service quota. This should
include an exception workflow in case of request deny or partial approval.
• Create an engineering method to review service quotas prior to provisioning and using new AWS
services before rolling out to production or loaded environments. (for example, load testing
account).
