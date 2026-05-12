---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 541
---

# Common anti-patterns:

• API endpoint throttles are not implemented or are left at default values without considering
expected volumes.
• API endpoints are not load tested or throttling limits are not tested.
• Throttling request rates without considering request size or complexity.
• Testing maximum request rates or maximum request size, but not testing both together.
• Resources are not provisioned to the same limits established in testing.
• Usage plans have not been configured or considered for application to application (A2A) API
consumers.
• Queue consumers that horizontally scale do not have maximum concurrency settings configured.
• Rate limiting on a per IP address basis has not been implemented.
Benefits of establishing this best practice: Workloads that set throttle limits are able to operate
normally and process accepted request load successfully under unexpected volume spikes. Sudden
or sustained spikes of requests to APIs and queues are throttled and do not exhaust request
processing resources. Rate limits throttle individual requestors so that high volumes of traffic from
a single IP address or API consumer will not exhaust resources impact other consumers.
Level of risk exposed if this best practice is not established: High
