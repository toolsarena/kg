---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 560
---

# Common anti-patterns:

• Only monitoring external interfaces to your workload.
• Not generating any workload-specific metrics and only relying on metrics provided to you by the
AWS services your workload uses.
• Only using technical metrics in your workload and not monitoring any metrics related to non-
technical KPIs the workload contributes to.
• Relying on production traffic and simple health checks to monitor and evaluate workload state.
Benefits of establishing this best practice: Monitoring at all tiers in your workload allows you to
more rapidly anticipate and resolve problems in the components that comprise the workload.
Level of risk exposed if this best practice is not established: High
