---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 667
---

# AWS Well-Architected Framework Framework

only minimally impacted). Use a combination of component faults to simulate events that may be
caused by a disruption in an Availability Zone.
For application-level faults (such as crashes), you can start with stressors such as memory and CPU
exhaustion.
To validate fallback or failover mechanisms for external dependencies due to intermittent network
disruptions, your components should simulate such an event by blocking access to the third-party
providers for a specified duration that can last from seconds to hours.
Other modes of degradation might cause reduced functionality and slow responses, often resulting
in a disruption of your services. Common sources of this degradation are increased latency on
critical services and unreliable network communication (dropped packets). Experiments with
these faults, including networking effects such as latency, dropped messages, and DNS failures,
could include the inability to resolve a name, reach the DNS service, or establish connections to
dependent services.
