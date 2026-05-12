---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 551
---

# AWS Well-Architected Framework Framework

• Not being aware of system timeouts or default timeouts.
• Not being aware of normal request completion timing.
• Not being aware of possible causes for requests to take abnormally long to complete, or the
costs to client, service, or workload performance associated with waiting on these completions.
• Not being aware of the probability of impaired network causing a request to fail only once
timeout is reached, and the costs to client and workload performance for not adopting a shorter
timeout.
• Not testing timeout scenarios both for connections and requests.
• Setting timeouts too high, which can result in long wait times and increase resource utilization.
• Setting timeouts too low, resulting in artificial failures.
• Overlooking patterns to deal with timeout errors for remote calls like circuit breakers and retries.
• Not considering monitoring for service call error rates, service level objectives for latency, and
latency outliers. These metrics can provide insight to aggressive or permissive timeouts
Benefits of establishing this best practice: Remote call timeouts are configured and systems are
designed to handle timeouts gracefully so that resources are conserved when remote calls respond
abnormally slow and timeout errors are handled gracefully by service clients.
Level of risk exposed if this best practice is not established: High
