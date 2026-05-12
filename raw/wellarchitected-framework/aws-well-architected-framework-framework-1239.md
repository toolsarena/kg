---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 635
---

# AWS Well-Architected Framework Framework

• Set alarms to detect when any part of your workload is not working properly and to indicate
when to automatically scale resources. Alarms can be visually displayed on dashboards, send
alerts through Amazon SNS or email, and work with Auto Scaling to scale workload resources up
or down.
• Create dashboards to visualize your metrics. Dashboards can be used to visually see trends,
outliers, and other indicators of potential problems or to provide an indication of problems you
may want to investigate.
• Create distributed tracing monitoring for your services. With distributed monitoring, you can
understand how your application and its underlying services are performing to identify and
troubleshoot the root cause of performance issues and errors.
• Create monitoring systems (using CloudWatch or X-Ray) dashboards and data collection in a
separate Region and account.
• Stay informed about service degradations with AWS Health. Create purpose-fit AWS Health
event notifications to e-mail and chat channels through AWS User Notifications and integrate
programmatically with your monitoring and alerting tools through Amazon EventBridge.
