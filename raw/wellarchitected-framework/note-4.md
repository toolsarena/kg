---
title: "Note"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 588
---

# Note

AWS has observed that with most applications, memory utilization increases as the
application warms up and then reaches a steady value. When demand decreases, memory
utilization typically remains elevated rather than decreasing in parallel. Because memory
utilization does not correspond to demand in both directions–that is, growing and falling
with demand–consider carefully before you select this metric for automatic scaling.
Metric-based scaling is a latent operation. It can take several minutes for utilization metrics to
propagate to auto scaling mechanisms, and these mechanisms typically wait for a clear signal
of increased demand before reacting. Then, as the auto scaler creates new resources, it can take
additional time for them to come to full service. Because of this, it is important to not set your
scaling metric targets too close to full utilization (for example, 90% CPU utilization). Doing so risks
exhausting existing resource capacity before additional capacity can come online. Typical resource
utilization targets can range between 50-70% for optimum availability, depending on demand
patterns and time required to provision additional resources.
