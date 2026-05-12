---
title: "Static stability of EC2 instances across Availability Zones"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 648
---

# Static stability of EC2 instances across Availability Zones

This must be weighed against the cost for this model and the business value of maintaining the
workload under all resilience cases. It's less expensive to provision less compute capacity and
rely on launching new instances in the case of a failure, but for large-scale failures (such as an
