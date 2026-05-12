---
title: "REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 537
---

# REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into

soft dependencies
Application components should continue to perform their core function even if dependencies
become unavailable. They might be serving slightly stale data, alternate data, or even no data. This
ensures overall system function is only minimally impeded by localized failures while delivering the
central business value.
Desired outcome: When a component's dependencies are unhealthy, the component itself can still
function, although in a degraded manner. Failure modes of components should be seen as normal
operation. Workflows should be designed in such a way that such failures do not lead to complete
failure or at least to predictable and recoverable states.
