---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 353
---

# Common anti-patterns:

• Teams independently own and manage logging and metrics collection that is inconsistent to the
organization's logging strategy.
• Teams don't have adequate access controls to restrict visibility and alteration of the data
collected.
• Teams don't govern their security logs, findings, and metrics as part of their data classification
policy.
• Teams neglect data sovereignty and localization requirements when configuring data collections.
Benefits of establishing this best practice: A standardized logging solution to collect and query
log data and events improves insights derived from the information they contain. Configuring an
automated lifecycle for the collected log data can reduce the costs incurred by log storage. You
can build fine-grained access control for the collected log information according to the sensitivity
of the data and access patterns needed by your teams. You can integrate tooling to correlate,
visualize, and derive insights from the data.
Level of risk exposed if this best practice is not established: Medium
