---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 230
---

# AWS Well-Architected Framework Framework

creating incidents in response to specific events from Amazon CloudWatch or Amazon EventBridge.
When an incident is created, either automatically or manually, Incident Manager centralizes
the management of the incident, organizes relevant AWS resource information, and initiates
predefined response plans. This includes running Systems Manager Automation runbooks for
immediate action, as well as creating a parent operational work item in OpsCenter to track related
tasks and analyses. This streamlined process speeds up and coordinates incident response across
your AWS environment.
