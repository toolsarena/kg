---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 537
---

# Common anti-patterns:

• Not identifying the core business functionality needed. Not testing that components are
functional even during dependency failures.
• Serving no data on errors or when only one out of multiple dependencies is unavailable and
partial results can still be returned.
• Creating an inconsistent state when a transaction partially fails.
• Not having an alternative way to access a central parameter store.
• Invalidating or emptying local state as a result of a failed refresh without considering the
consequences of doing so.
