---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 491
---

# AWS Well-Architected Framework Framework

• Determine your service quotas. Account for typical deployment patterns, availability
requirements, and consumption growth.
• Request quota increases if necessary. Anticipate a wait time for the quota increase request.
• Determine your reliability requirements (also known as your number of nines).
• Understand potential fault scenarios such as loss of a component, an Availability Zone, or a
Region.
• Establish your deployment methodology (examples include canary, blue/green, red/black, and
rolling).
• Include an appropriate buffer to the current quota limit. An example buffer could be 15%.
• Include calculations for static stability (Zonal and Regional) where appropriate.
• Plan consumption growth and monitor your consumption trends.
• Consider the static stability impact for your most critical workloads. Assess resources conforming
to a statically stable system in all Regions and Availability Zones.
• Consider using On-Demand Capacity Reservations to schedule capacity ahead of any failover.
This is a useful strategy to implement for critical business schedules to reduce potential risks of
obtaining the correct quantity and type of resources during failover.
