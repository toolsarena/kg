---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 477
---

# Implementation steps

• Review Service Quotas values that might have breached beyond the a risk level of usage. AWS
Trusted Advisor provides alerts for 80% and 90% threshold breaches.
• Review values for service quotas in any Passive Regions (in an Active/Passive design). Verify that
load will successfully run in secondary Regions in the event of a failure in the primary Region.
• Automate assessing if any service quota drift has occurred between Regions in the same account
and act accordingly to change the limits.
• If the customer Organizational Units (OU) are structured in the supported manner, service quota
templates should be updated to reflect changes in any quotas that should be applied to multiple
Regions and accounts.
• Create a template and associate Regions to the quota change.
• Review all existing service quota templates for any changes required (Region, limits, and
accounts).
