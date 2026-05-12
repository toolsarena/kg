---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 480
---

# AWS Well-Architected Framework Framework

• Choosing a design that cannot scale or be modified if fixed service quotas are to be exceeded.
For example, an SQS payload size of 256KB.
• Observability has not been designed and implemented to monitor and alert on thresholds for
service quotas that might be at risk during high traffic events
Benefits of establishing this best practice: Verifying that the application will run under all
projected services load levels without disruption or degradation.
Level of risk exposed if this best practice is not established: Medium
