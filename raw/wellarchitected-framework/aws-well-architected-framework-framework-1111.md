---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 477
---

# AWS Well-Architected Framework Framework

Service quota drift, the condition where service quota limits for a specific named quota is changed
in one Region and not all Regions, is very important to track and assess. Changing the quota in
Regions with traffic or potentially could carry traffic should be considered.
• Select relevant accounts and Regions based on your service requirements, latency, regulatory,
and disaster recovery (DR) requirements.
• Identify service quotas across all relevant accounts, Regions, and Availability Zones. The limits
are scoped to account and Region. These values should be compared for differences.
