---
title: "Note"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 687
---

# Note

The difference between pilot light and warm standby can sometimes be difficult to
understand. Both include an environment in your recovery Region with copies of your
primary region assets. The distinction is that pilot light cannot process requests without
additional action taken first, while warm standby can handle traffic (at reduced capacity
levels) immediately. Pilot light will require you to turn on servers, possibly deploy
additional (non-core) infrastructure, and scale up, while warm standby only requires you
to scale up (everything is already deployed and running). Choose between these based on
your RTO and RPO needs.
When cost is a concern, and you wish to achieve a similar RPO and RTO objectives as
defined in the warm standby strategy, you could consider cloud native solutions, like AWS
Elastic Disaster Recovery, that take the pilot light approach and offer improved RPO and
RTO targets.


# Note

Some workloads have regulatory data residency requirements. If this applies to your
workload in a locality that currently has only one AWS Region, then multi-Region will
not suit your business needs. Multi-AZ strategies provide good protection against most
disasters.

# Note

Some languages may require you to implement your own in-memory encryption for client
side caching.