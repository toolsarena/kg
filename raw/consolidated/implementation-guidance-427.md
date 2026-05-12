---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 490
---

# Implementation guidance

When evaluating a quota limit, consider failover cases that might occur due to some degradation.
Consider the following failover cases.
• A disrupted or inaccessible VPC.
• An inaccessible subnet.
• A degraded Availability Zone that impacts resource accessibility.
• Networking routes or ingress and egress points are blocked or changed.
• A degraded Region that impacts resource accessibility.
• A subset of resources affected by a failure in a Region or an Availability Zone.
The decision to failover is unique for each situation, as the business impact can vary. Address
resource capacity planning in the failover location and the resources’ quotas before deciding to
failover an application or service.
Consider higher than normal peaks of activity when reviewing quotas for each service. These peaks
might be related to resources that are inaccessible due to networking or permissions, but are still
active. Unterminated active resources count against the service quota limit.
