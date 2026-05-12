---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 144
---

# Implementation guidance

Implement dependency telemetry by starting with identifying the services, infrastructure, and
processes that your workload depends on. Quantify what good conditions look like when those
dependencies are functioning as expected, and then determine what data will be needed to
measure those. With that information you can craft dashboards and alerts that provide insights to
your operations teams on the state of those dependencies. Use AWS tools to discover and quantify
the impacts when dependencies cannot deliver as needed. Continually revisit your strategy to
account for changes in priorities, goals, and gained insights.


# Implementation guidance

A consistent, documented policy and practice adopted by release teams allows an organization
to plan what should happen if unsuccessful changes occur. The policy should allow for fixing