---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 545
---

# Common anti-patterns:

• Implementing retries without adding exponential backoff, jitter, and maximum retry values.
Backoff and jitter help avoid artificial traffic spikes due to unintentionally coordinated retries at
common intervals.
• Implementing retries without testing their effects or assuming retries are already built into an
SDK without testing retry scenarios.
• Failing to understand published error codes from dependencies, leading to retrying all errors,
including those with a clear cause that indicates lack of permission, configuration error, or
another condition that predictably will not resolve without manual intervention.
• Not addressing observability practices, including monitoring and alerting on repeated service
failures so that underlying issues are made known and can be addressed.
• Developing custom retry mechanisms when built-in or third-party retry capabilities suffice.
• Retrying at multiple layers of your application stack in a manner which compounds retry
attempts further consuming resources in a retry storm. Be sure to understand how these errors
affect your application the dependencies you rely on, then implement retries at only one level.
• Retrying service calls that are not idempotent, causing unexpected side effects like duplicated
results.
Benefits of establishing this best practice: Retries help clients acquire desired results when
requests fail but also consume more of a server’s time to get the successful responses they
want. When failures are rare or transient, retries work well. When failures are caused by resource
overload, retries can make things worse. Adding exponential backoff with jitter to client retries
allows servers to recover when failures are caused by resource overload. Jitter avoids alignment
of requests into spikes, and backoff diminishes load escalation caused by adding retries to normal
request load. Finally, it’s important to configure a maximum number of retries or elapsed time to
avoid creating backlogs that produce metastable failures.
Level of risk exposed if this best practice is not established: High
