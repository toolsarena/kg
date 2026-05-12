---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 701
---

# AWS Well-Architected Framework Framework

To achieve consistency between your primary and disaster recovery (DR) environments, validate
that your delivery pipelines distribute applications to both your primary and DR sites. Roll
out changes to the DR sites after an appropriate evaluation period (also known as staggered
deployments) to detect problems at the primary site and halt the deployment before they spread.
Implement monitoring to detect configuration drift, and track changes and compliance across your
environments. Perform automated remediation in the DR site to keep it fully consistent and ready
to take over in the event of an incident.
