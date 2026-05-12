---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 918
---

# AWS Well-Architected Framework Framework

Buffering and throttling can smooth out any peaks by modifying the demand on your workload.
Use throttling when clients retry actions and use buffering to hold the request and process it later.
When working with a buffer-based approach, architect your workload to service the request in the
required time, verify that you are able to handle duplicate requests for work. Analyze the overall
demand, rate of change, and required response time to right size the throttle or buffer required.
