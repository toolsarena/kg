---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 652
---

# Implementation steps

Create various types of alarms based on how the workloads are monitored, such as:
• Application alarms are used to detect when any part of your workload is not working properly.
• Infrastructure alarms indicate when to scale resources. Alarms can be visually displayed on
dashboards, send alerts through Amazon SNS or email, and work with Auto Scaling to scale
workload resources in or out.
• Simple static alarms can be created to monitor when a metric breaches a static threshold for a
specified number of evaluation periods.
