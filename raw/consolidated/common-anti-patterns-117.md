---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 479
---

# Common anti-patterns:

• Choosing a design that uses a resource of a service, unaware that there are design constraints
that will cause this design to fail as you scale.
• Performing benchmarking that is unrealistic and will reach service fixed quotas during the
testing. For example, running tests at a burst limit but for an extended amount of time.
