---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 699
---

# AWS Well-Architected Framework Framework

test this failover, you might find that your assumptions about the capabilities of the secondary
data store are incorrect. The capacity of the secondary, which might have been sufficient when you
last tested, might be no longer be able to tolerate the load under this scenario. Our experience has
shown that the only error recovery that works is the path you test frequently. This is why having
a small number of recovery paths is best. You can establish recovery patterns and regularly test
them. If you have a complex or critical recovery path, you still need to regularly exercise that failure
in production to convince yourself that the recovery path works. In the example we just discussed,
you should fail over to the standby regularly, regardless of need.
