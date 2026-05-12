---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 799
---

# Common anti-patterns:

• You load test individual parts of your workload but not your entire workload.
• You load test on infrastructure that is not the same as your production environment.
• You only conduct load testing to your expected load and not beyond, to help foresee where you
may have future problems.
• You perform load testing without consulting the Amazon EC2 Testing Policy and submitting
a Simulated Event Submissions Form. This results in your test failing to run, as it looks like a
denial-of-service event.
