---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 488
---

# AWS Well-Architected Framework Framework

integrate your configuration management databases (CMDB) and IT service management (ITSM)
systems with the AWS Service Quota APIs.
Generate automated alerts if quota usage reaches your defined thresholds, and define a process for
submitting quota increase requests when you receive alerts. If the underlying workload is critical
to your business, you can automate quota increase requests, but carefully test the automation to
avoid the risk of runaway action such as a growth feedback loop.
Smaller quota increases are often automatically approved. Larger quota requests may need to be
manually processed by AWS support and can take additional time to review and process. Allow for
additional time to process multiple requests or large increase requests.
