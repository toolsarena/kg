---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 282
---

# AWS Well-Architected Framework Framework

• Making changes to your standard security controls manually, through a web console or
command-line interface.
• Relying on individual workload teams to manually implement the controls a central team
defines.
• Relying on a central security team to deploy workload-level controls at the request of a workload
team.
• Allowing the same individuals or teams to develop, test, and deploy security control automation
scripts without proper separation of duties or checks and balances.
Benefits of establishing this best practice: Using templates to define your standard security
controls allows you to track and compare changes over time using a version control system. Using
automation to test and deploy changes creates standardization and predictability, increasing
the chances of a successful deployment and reducing manual repetitive tasks. Providing a self-
serve mechanism for workload teams to deploy approved services and configurations reduces the
risk of misconfiguration and misuse. This also helps them to incorporate controls earlier in the
development process.
Level of risk exposed if this best practice is not established: Medium
