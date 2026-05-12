---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 155
---

# Common anti-patterns:

• You manually update the web server configuration across your fleet and a number of servers
become unresponsive due to update errors.
• You manually update your application server fleet over the course of many hours. The
inconsistency in configuration during the change causes unexpected behaviors.
• Someone has updated your security groups and your web servers are no longer accessible.
Without knowledge of what was changed you spend significant time investigating the issue
extending your time to recovery.
• You push a pre-production configuration into production through CI/CD without validation. You
expose users and customers to incorrect data and services.
Benefits of establishing this best practice: Adopting configuration management systems reduces
the level of effort to make and track changes, and the frequency of errors caused by manual
procedures. Configuration management systems provide assurances with regards to governance,
compliance, and regulatory requirements.
Level of risk exposed if this best practice is not established: Medium
