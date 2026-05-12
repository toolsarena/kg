---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 508
---

# Implementation steps

• Capture current CIDR consumption (for example, VPCs and subnets).
• Use service API operations to collect current CIDR consumption.
• Use the Amazon VPC IP Address Manager to discover resources.
• Capture your current subnet usage.
• Use service API operations to collect subnets per VPC in each Region.
• Use the Amazon VPC IP Address Manager to discover resources.
• Record the current usage.
• Determine if you created any overlapping IP ranges.
• Calculate the spare capacity.
• Identify overlapping IP ranges. You can either migrate to a new range of addresses or consider
using techniques like private NAT Gateway or AWS PrivateLink if you need to connect the
overlapping ranges.
