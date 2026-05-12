---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 483
---

# Common anti-patterns:

• Not configuring monitoring to check for service quota thresholds
• Not configuring monitoring for hard limits, even though those values cannot be changed.
• Assuming that amount of time required to request and secure a soft quota change is immediate
or a short period.
• Configuring alarms for when service quotas are being approached, but having no process on how
to respond to an alert.
• Only configuring alarms for services supported by AWS Service Quotas and not monitoring other
AWS services.
• Not considering quota management for multiple Region resiliency designs, like active/active,
active/passive – hot, active/passive - cold, and active/passive - pilot light approaches.
• Not assessing quota differences between Regions.
• Not assessing the needs in every Region for a specific quota increase request.
• Not leveraging templates for multi-Region quota management.
Benefits of establishing this best practice: Automatic tracking of the AWS Service Quotas and
monitoring your usage against those quotas will allow you to see when you are approaching a
quota limit. You can also use this monitoring data to help limit any degradations due to quota
exhaustion.
Level of risk exposed if this best practice is not established: Medium
