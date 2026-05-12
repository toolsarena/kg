---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 169
---

# Common anti-patterns:

• You are performing development in a shared development environment and another developer
overwrites your code changes.
• The restrictive security controls on your shared development environment are preventing you
from experimenting with new services and features.
• You perform load testing on your production systems and cause an outage for your users.
• A critical error resulting in data loss has occurred in production. In your production environment,
you attempt to recreate the conditions that lead to the data loss so that you can identify how it
happened and prevent it from happening again. To prevent further data loss during testing, you
are forced to make the application unavailable to your users.
• You are operating a multi-tenant service and are unable to support a customer request for a
dedicated environment.
• You may not always test, but when you do, you test in your production environment.
• You believe that the simplicity of a single environment overrides the scope of impact of changes
within the environment.
• You upgrade a key landing zone capability, but the change impairs your team's ability to vend
accounts for either new projects or your existing workloads.
• You apply new controls to your AWS accounts, but the change impacts your workload team's
ability to deploy changes within their AWS accounts.
Benefits of establishing this best practice: When you deploy multiple environments, you can
support multiple simultaneous development, testing, and production environments without
creating conflicts between developers or user communities. For complex capabilities such as
landing zones, it significantly reduces the risk of changes, simplifies the improvement process,
and reduces the risk of critical updates to the environment. Organizations that use landing
zones naturally benefit from multi-accounts in their AWS environment, with account structure,


# Common anti-patterns:

• Overlooking trace data, relying solely on logs and metrics.
• Not correlating trace data with associated logs.
• Ignoring the metrics derived from traces, such as latency and fault rates.

# Common anti-patterns:

• Setting up too many non-critical alerts, leading to alert fatigue.
• Not prioritizing alerts based on KPIs, making it hard to understand the business impact of issues.
• Neglecting to address root causes, leading to repetitive alerts for the same issue.