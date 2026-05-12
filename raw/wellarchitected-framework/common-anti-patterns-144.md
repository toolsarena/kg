---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 586
---

# Common anti-patterns:

• You provision a fixed number of scalable resources.
• You choose a scaling metric that does not correlate to actual demand.
• You fail to provide enough headroom in your scaling plans to accommodate demand bursts.
• Your scaling policies add capacity too late, which leads to capacity exhaustion and degraded
service while additional resources are brought online.
• You fail to correctly configure minimum and maximum resource counts, which leads to scaling
failures.
Benefits of establishing this best practice: Having enough resources to meet current demand
is critical to provide high availability of your workload and adhere to your defined service-level
objectives (SLOs). Automatic scaling allows you to provide the right amount of compute, database,
and other resources your workload needs in order to serve current and forecasted demand. You
don't need to determine peak capacity needs and statically allocate resources to serve it. Instead,
as demand grows, you can allocate more resources to accommodate it, and after demand falls, you
can deactivate resources to reduce cost.
