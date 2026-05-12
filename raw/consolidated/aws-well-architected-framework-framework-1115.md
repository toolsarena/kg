---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 481
---

# AWS Well-Architected Framework Framework

objects. Let your business and technology drivers guide the process to identify the distributed
system that is right for your workload.
• Analyze service load across Regions and accounts. Many hard limits are regionally based for
services. However, some limits are account based.
• Analyze resilience architectures for resource usage during a zonal failure and Regional failure. In
the progression of multi-Region designs using active/active, active/passive – hot, active/passive -
cold, and active/passive - pilot light approaches, these failure cases will cause higher usage. This
creates a potential use case for hitting hard limits.
