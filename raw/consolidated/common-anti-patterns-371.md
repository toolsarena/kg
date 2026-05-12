---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 578
---

# Common anti-patterns:

• Tracing is used for some components but not for all. For example, without tracing for AWS
Lambda, teams might not clearly understand latency caused by cold starts in a spiky workload.
• Synthetic canaries or real-user monitoring (RUM) are not configured with tracing. Without
canaries or RUM, client interaction telemetry is omitted from the trace analysis yielding an
incomplete performance profile.
• Hybrid workloads include both cloud native and third party tracing tools, but steps have not
been taken elect and fully integrate a single tracing solution. Based on the elected tracing
solution, cloud native tracing SDKs should be used to instrument components that are not cloud
native or third party tools should be configured to ingest cloud native trace telemetry.
Benefits of establishing this best practice: When development teams are alerted to issues, they
can see a full picture of system component interactions, including component by component
correlation to logging, performance, and failures. Because tracing makes it easy to visually identify
root causes, less time is spent investigating root causes. Teams that understand component
interactions in detail make better and faster decisions when resolving issues. Decisions like when
to invoke disaster recovery (DR) failover or where to best implement self-healing strategies can
be improved by analyzing systems traces, ultimately improving customer satisfaction with your
services.
