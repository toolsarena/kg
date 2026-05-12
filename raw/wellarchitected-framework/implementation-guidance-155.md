---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 579
---

# Implementation guidance

Teams that operate distributed applications can use tracing tools to establish a correlation
identifier, collect traces of requests, and build service maps of connected components. All
application components should be included in request traces including service clients, middleware
gateways and event buses, compute components, and storage, including key value stores and
databases. Include synthetic canaries and real-user monitoring in your end-to-end tracing
configuration to measure remote client interactions and latency so that you can accurately
evaluate your systems performance against your service level agreements and objectives.
You can use AWS X-Ray and Amazon CloudWatch Application Monitoring instrumentation services
to provide a complete view of requests as they travel through your application. X-Ray collects
application telemetry and allows you to visualize and filter it across payloads, functions, traces,
services, APIs, and can be turned on for system components with no-code or low-code. CloudWatch
application monitoring includes ServiceLens to integrate your traces with metrics, logs, and alarms.
CloudWatch application monitoring also includes synthetics to monitor your endpoints and APIs, as
well as real-user monitoring to instrument your web application clients.
