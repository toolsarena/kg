---
title: "Figure 21: Warm standby architecture"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 691
---

# Figure 21: Warm standby architecture

Using warm standby or pilot light requires scaling up resources in the recovery Region. To verify
capacity is available when needed, consider the use for capacity reservations for EC2 instances.
If using AWS Lambda, then provisioned concurrency can provide runtime environments so that
they are prepared to respond immediately to your function's invocations.
For more details on this strategy, see Disaster Recovery (DR) Architecture on AWS, Part III: Pilot
Light and Warm Standby.


# Figure 22: Multi-site active/active architecture

For more details on this strategy, see Disaster Recovery (DR) Architecture on AWS, Part IV: Multi-
site Active/Active.

# Figure 22: Multi-site active/active architecture

For more details on this strategy, see Disaster Recovery (DR) Architecture on AWS, Part IV: Multi-
site Active/Active.