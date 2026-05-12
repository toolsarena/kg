---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 655
---

# Implementation steps

• Review and document the workload design considering the following questions:
• Where are control planes used in the workload?
• How does the workload implement fault tolerance?
• What are the design patterns for scaling, automatic scaling, redundancy, and highly available
components?
• What are the requirements for data consistency and availability?
• Are there considerations for resource sparing or resource static stability?
• What are the service dependencies?
• Define SLA metrics based on the workload architecture while working with stakeholders.
Consider the SLAs of all dependencies used by the workload.
• Once the SLA target has been set, optimize the architecture to meet the SLA.
• Once the design is set that will meet the SLA, implement operational changes, process
automation, and runbooks that also will have focus on reducing MTTD and MTTR.
• Once deployed, monitor and report on the SLA.
