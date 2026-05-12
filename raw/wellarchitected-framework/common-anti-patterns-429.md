---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 806
---

# Common anti-patterns:

• You allow metrics to stay in an alarm state for an extended period of time.
• You create alarms that are not actionable by an automation system.
Benefits of establishing this best practice: Continually review metrics that are being collected to
verify that they properly identify, address, or prevent issues. Metrics can also become stale if you
let them stay in an alarm state for an extended period of time.
Level of risk exposed if this best practice is not established: Medium
