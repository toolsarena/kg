---
title: "Related tools:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 643
---

# Related tools:

• CloudWatch
• CloudWatch X-Ray
REL11-BP04 Rely on the data plane and not the control plane during recovery
Control planes provide the administrative APIs used to create, read and describe, update,
delete, and list (CRUDL) resources, while data planes handle day-to-day service traffic. When
implementing recovery or mitigation responses to potentially resiliency-impacting events, focus on
using a minimal number of control plane operations to recover, rescale, restore, heal, or failover the
service. Data plane action should supersede any activity during these degradation events.


# Related tools:

• Amazon CloudWatch
• AWS X-Ray