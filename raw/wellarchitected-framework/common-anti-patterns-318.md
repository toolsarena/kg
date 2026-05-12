---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 372
---

# Common anti-patterns:

• Relying on individual workload teams to each define their complete network stack, protections,
and automations. Not publishing standard aspects of the network stack and protections
centrally for workload teams to consume.
• Relying on a central network team to define all aspects of the network, protections, and
automations. Not delegating workload-specific aspects of the network stack and protections to
that workload's team.
• Striking the right balance between centralization and delegation between a network team and
workload teams, but not applying consistent testing and deployment standards across your IaC
templates and CI/CD pipelines. Not capturing required configurations in tooling that checks your
templates for adherence.
Benefits of establishing this best practice: Using templates to define your network protections
allows you to track and compare changes over time with a version control system. Using
automation to test and deploy changes creates standardization and predictability, increasing the
chances of a successful deployment and reducing repetitive manual configurations.
Level of risk exposed if this best practice is not established: Medium
