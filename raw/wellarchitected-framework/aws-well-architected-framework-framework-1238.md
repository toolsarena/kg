---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 634
---

# AWS Well-Architected Framework Framework

monitoring interval. The monitoring interval will have a direct impact on how fast recovery can be
initiated based on the time it takes to detect a failure. The mean time to detection (MTTD) is the
amount of time between a failure occurring and when repair operations begin. The list of services
should be extensive and complete.
Monitoring must cover all layers of the application stack including application, platform,
infrastructure, and network.
Your monitoring strategy should consider the impact of gray failures. For more detail on gray
failures, see Gray failures in the Advanced Multi-AZ Resilience Patterns whitepaper.
