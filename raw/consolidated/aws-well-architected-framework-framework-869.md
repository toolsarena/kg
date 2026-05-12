---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 155
---

# AWS Well-Architected Framework Framework

configuration should be managed independently of application and infrastructure code. This allows
for consistent deployment across multiple environments. Configuration changes do not result in
rebuilding or redeploying the application.
Desired outcome: You configure, validate, and deploy as part of your continuous integration,
continuous delivery (CI/CD) pipeline. You monitor to validate configurations are correct. This
minimizes any impact to end users and customers.
