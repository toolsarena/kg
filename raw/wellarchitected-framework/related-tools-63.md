---
title: "Related tools:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 489
---

# Related tools:

• Quota Monitor for AWS
REL01-BP06 Ensure that a sufficient gap exists between the current quotas and the maximum
usage to accommodate failover
This article explains how to maintain space between the resource quota and your usage, and
how it can benefit your organization. After you finish using a resource, the usage quota may
continue to account for that resource. This can result in a failing or inaccessible resource. Prevent
resource failure by verifying that your quotas cover the overlap of inaccessible resources and their
replacements. Consider cases like network failure, Availability Zone failure, or Region failures when
calculating this gap.
Desired outcome: Small or large failures in resources or resource accessibility can be covered
within the current service thresholds. Zone failures, network failures, or even Regional failures have
been considered in the resource planning.
