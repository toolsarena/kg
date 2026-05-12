---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 539
---

# Implementation steps

Identify external and internal dependencies. Consider what kinds of failures can occur in them.
Think about ways that minimize negative impact on upstream and downstream systems and
customers during those failures.
The following is a list of dependencies and how to degrade gracefully when they fail:
1. Partial failure of dependencies: A component may make multiple requests to downstream
systems, either as multiple requests to one system or one request to multiple systems each.
Depending on the business context, different ways of handling for this may be appropriate (for
more detail, see previous examples in Implementation guidance).
2. A downstream system is unable to process requests due to high load: If requests to a
downstream system are consistently failing, it does not make sense to continue retrying.
This may create additional load on an already overloaded system and make recovery more
difficult. The circuit breaker pattern can be utilized here, which monitors failing calls to a
downstream system. If a high number of calls are failing, it will stop sending more requests to
the downstream system and only occasionally let calls through to test whether the downstream
system is available again.
3. A parameter store is unavailable: To transform a parameter store, soft dependency caching or
sane defaults included in container or machine images may be used. Note that these defaults
need to be kept up-to-date and included in test suites.
4. A monitoring service or other non-functional dependency is unavailable: If a component is
intermittently unable to send logs, metrics, or traces to a central monitoring service, it is often
best to still execute business functions as usual. Silently not logging or pushing metrics for a
