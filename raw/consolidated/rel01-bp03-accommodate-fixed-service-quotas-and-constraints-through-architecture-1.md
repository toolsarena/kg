---
title: "REL01-BP03 Accommodate fixed service quotas and constraints through architecture"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 479
---

# REL01-BP03 Accommodate fixed service quotas and constraints through architecture

Be aware of unchangeable service quotas, service constraints, and physical resource limits. Design
architectures for applications and services to prevent these limits from impacting reliability.
Examples include network bandwidth, serverless function invocation payload size, throttle burst
rate for of an API gateway, and concurrent user connections to a database.
Desired outcome: The application or service performs as expected under normal and high traffic
conditions. They have been designed to work within the limitations for that resource’s fixed
constraints or service quotas.
