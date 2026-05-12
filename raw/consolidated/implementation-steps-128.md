---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 623
---

# Implementation steps

1. Work with business stakeholders and data residency experts to determine which AWS Regions
can be used to host your resources and data.
2. Work with business and technical stakeholders to evaluate your workload, and determine
whether its resilience needs can be met by a multi-AZ approach (single AWS Region) or if they
require a multi-Region approach (if multiple Regions are permitted). The use of multiple Regions
can achieve greater availability but can involve additional complexity and cost. Consider the
following factors in your evaluation:
a. Business objectives and customer requirements: How much downtime is permitted should a
workload-impacting incident occur in an Availability Zone or a Region? Evaluate your recovery
point objectives as discussed in REL13-BP01 Define recovery objectives for downtime and
data loss.
b. Disaster recovery (DR) requirements: What kind of potential disaster do you want to
insure yourself against? Consider the possibility of data loss or long-term unavailability at
different scopes of impact from a single Availability Zone to an entire Region. If you replicate
data and resources across Availability Zones, and a single Availability Zone experiences a
sustained failure, you can recover service in another Availability Zone. If you replicate data
and resources across Regions, you can recover service in another Region.
3. Deploy your compute resources into multiple Availability Zones.
a. In your VPC, create multiple subnets in different Availability Zones. Configure each to be
large enough to accommodate the resources needed to serve the workload, even during an
incident. For more detail, see REL02-BP03 Ensure IP subnet allocation accounts for expansion
and availability.
