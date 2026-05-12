---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 571
---

# Common anti-patterns:

• Not having a clear inventory or catalog of key real-time alarms.
• No automated responses on critical alarms (for example, when compute is nearing exhaustion,
autoscaling occurs).
• Contradictory alarm response actions.
• No standard operating procedures (SOPs) for operators to follow when they receive alert
notifications.
• Not monitoring configuration changes, as undetected configuration changes can cause
downtime for workloads.
• Not having a strategy to undo unintended configuration changes.
Benefits of establishing this best practice: Automating alarm processing can improve system
resiliency. The system takes corrective actions automatically, reducing manual activities that allow
for human, error-prone interventions. Workload operates meet availability goals, and reduces
service disruption.
Level of risk exposed if this best practice is not established: Medium
