---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 703
---

# Common anti-patterns:

• You depend on components or mechanisms that are in a failed or degraded state as part of your
recovery plan.
• Your recovery processes require manual intervention, such as console access (also known as click
ops).
• You automatically initiate recovery procedures in situations that present a high risk of data loss
or unavailability.
• You fail to include a mechanism to abort a recovery procedure (like an Andon cord or big red stop
button) that is not working or that poses additional risks.
