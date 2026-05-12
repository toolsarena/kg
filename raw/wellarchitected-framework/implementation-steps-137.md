---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 660
---

# Implementation steps

• While conducting post-incident analysis, ensure the process is blame-free. This allows people
involved in the incident to be dispassionate about the proposed corrective actions and promote
honest self-assessment and collaboration across teams.
• Define a standardized way to document critical issues. An example structure for such document
is as follows:
• What happened?
• What was the impact on customers and your business?
• What was the root cause?
• What data do you have to support this?
• For example, metrics and graphs
• What were the critical pillar implications, especially security?
• When architecting workloads, you make trade-offs between pillars based upon your business
context. These business decisions can drive your engineering priorities. You might optimize
to reduce cost at the expense of reliability in development environments, or, for mission-
critical solutions, you might optimize reliability with increased costs. Security is always job
zero, as you have to protect your customers.
• What lessons did you learn?
• What corrective actions are you taking?
