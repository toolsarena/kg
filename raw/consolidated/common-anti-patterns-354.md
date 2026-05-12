---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 507
---

# Common anti-patterns:

• Using the same IP range in your VPC as you have on premises, in your corporate network, or
other cloud providers
• Not tracking IP ranges of VPCs used to deploy your workloads.
• Relying on manual IP address management processes, such as spreadsheets.
• Over- or under-sizing CIDR blocks, which results in IP address waste or insufficient address space
for your workload.


# Common anti-patterns:

• The microservice Death Star is a situation in which the atomic components become so highly
interdependent that a failure of one results in a much larger failure, making the components as
rigid and fragile as a monolith.