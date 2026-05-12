---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 555
---

# Implementation guidance

Make your applications stateless. Stateless applications allow horizontal scaling and are tolerant to
the failure of an individual node. Analyze and understand the components of your application that
maintain state within the architecture. This helps you assess the potential impact of transitioning
to a stateless design. A stateless architecture decouples user data and offloads the session data.
This provides the flexibility to scale each component independently to meet varying workload
demands and optimize resource utilization.
