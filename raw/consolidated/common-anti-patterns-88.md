---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 369
---

# Common anti-patterns:

• Relying solely on firewall rules based on ports and protocols. Not taking advantage of intelligent
systems.
• Authoring firewall rules based on specific current threat patterns that are subject to change.
• Only inspecting traffic where traffic transits from private to public subnets, or from public
subnets to the Internet.
• Not having a baseline view of your network traffic to compare for behavior anomalies.
Benefits of establishing this best practice: Inspection systems allow you to author intelligent
rules, such as allowing or denying traffic only when certain conditions within the traffic data exist.
Benefit from managed rule sets from AWS and partners, based on the latest threat intelligence,
as the threat landscape changes over time. This reduces the overhead of maintaining rules and
researching indicators of compromise, reducing the potential for false positives.
Level of risk exposed if this best practice is not established: Medium
