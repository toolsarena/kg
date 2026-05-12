---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 865
---

# Implementation guidance

Decommission workload resources that are no longer required. A common example is resources
used for testing: after testing has been completed, the resources can be removed. Tracking
resources with tags (and running reports on those tags) can help you identify assets for
decommission, as they will not be in use or the license on them will expire. Using tags is an
effective way to track resources, by labeling the resource with its function, or a known date when
it can be decommissioned. Reporting can then be run on these tags. Example values for feature
tagging are feature-X testing to identify the purpose of the resource in terms of the workload
lifecycle. Another example is using LifeSpan or TTL for the resources, such as to-be-deleted tag
key name and value to define the time period or specific time for decommissioning.


# Implementation guidance

Implement a standardized process across your organization to identify and remove unused
resources. The process should define the frequency searches are performed and the processes to
remove the resource to verify that all organization requirements are met.