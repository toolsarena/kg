---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 547
---

# Common anti-patterns:

• Implementing message queues but not configuring dead letter queues (DLQ) or alarms on DLQ
volumes to detect when a system is in failure.
• Not measuring the age of messages in a queue, a measurement of latency to understand when
queue consumers are falling behind or erroring out causing retrying.
