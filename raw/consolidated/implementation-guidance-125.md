---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 476
---

# Implementation guidance

Service quotas are tracked per account. Unless otherwise noted, each quota is AWS Region-specific.
In addition to the production environments, also manage quotas in all applicable non-production
environments so that testing and development are not hindered. Maintaining a high degree of
resiliency requires that service quotas are assessed continually (whether automated or manual).
With more workloads spanning Regions due to the implementation of designs using Active/Active,
Active/Passive – Hot, Active/Passive-Cold, and Active/Passive-Pilot Light approaches, it is essential
to understand all Region and account quota levels. Past traffic patterns are not always a good
indicator if the service quota is set correctly.
Equally important, the service quota name limit is not always the same for every Region. In one
Region, the value could be five, and in another region the value could be ten. Management of these
quotas must span all the same services, accounts, and Regions to provide consistent resilience
under load.
Reconcile all the service quota differences across different Regions (Active Region or Passive
Region) and create processes to continually reconcile these differences. The testing plans of passive
Region failovers are rarely scaled to peak active capacity, meaning that game day or table top
exercises can fail to find differences in service quotas between Regions and also then maintain the
correct limits.
