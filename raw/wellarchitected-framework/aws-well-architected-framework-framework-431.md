---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 565
---

# AWS Well-Architected Framework Framework

Querying logs can help you understand how specific requests were handled by your workload
components and reveal request patterns or other context that has an impact on your workload's
resilience. It can be useful to research and prepare queries in advance, based on your knowledge of
how your applications and other components behave, so you can more easily run them as needed.
For example, with CloudWatch Logs Insights, you can interactively search and analyze your log data
stored in CloudWatch Logs. You can also use Amazon Athena to query logs from multiple sources,
including many AWS services, at petabyte scale.
When you define a log retention policy, consider the value of historical logs. Historical logs can
help identify long-term usage and behavioral patterns, regressions, and improvements in your
workload's performance. Permanently deleted logs cannot be analyzed later. However, the value
of historical logs tends to diminish over long periods of time. Choose a policy that balances your
needs as appropriate and is compliant with any legal or contractual requirements you might be
subject to.
