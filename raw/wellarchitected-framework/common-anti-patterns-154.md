---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 629
---

# Common anti-patterns:

• Allowing cells to grow without bounds.
• Applying code updates or deployments to all cells at the same time.
• Sharing state or components between cells (with the exception of the router layer).
• Adding complex business or routing logic to the router layer.
• Not minimizing cross-cell interactions.
Benefits of establishing this best practice: With cell-based architectures, many common types
of failure are contained within the cell itself, providing additional fault isolation. These fault
boundaries can provide resilience against failure types that otherwise are hard to contain, such as
unsuccessful code deployments or requests that are corrupted or invoke a specific failure mode
(also known as poison pill requests).
Level of risk exposed if this best practice is not established: High
