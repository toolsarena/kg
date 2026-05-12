---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 218
---

# Common anti-patterns:

• Deployment deadlines are missed because developers are pulled away to perform
troubleshooting tasks. Development teams argue for more personnel, but cannot quantify how
many they need because the time taken away cannot be measured.
• A Tier 1 desk was set up to handle user calls. Over time, more workloads were added, but no
headcount was allocated to the Tier 1 desk. Customer satisfaction suffers as call times increase
and issues go longer without resolution, but management sees no indicators of such, preventing
any action.
• A problematic workload has been handed off to a separate operations team for upkeep. Unlike
other workloads, this new one was not supplied with proper documentation and runbooks. As
such, teams spend longer troubleshooting and addressing failures. However, there are no metrics
documenting this, which makes accountability difficult.
Benefits of establishing this best practice: Where workload monitoring shows the state
of our applications and services, monitoring operations teams provides owners insight into
changes among the consumers of those workloads, such as shifting business needs. Measure the
effectiveness of these teams and evaluate them against business goals by creating metrics that can
reflect the state of operations. Metrics can highlight support issues or identify when drifts occur
away from a service level target.
Level of risk exposed if this best practice is not established: Medium
