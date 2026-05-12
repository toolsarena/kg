---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 630
---

# Implementation steps

When designing a cell-based architecture, there are several design considerations to consider:
1. Partition key: Special consideration should be taken while choosing the partition key.
• It should align with the grain of the service, or the natural way that a service's workload can
be subdivided with minimal cross-cell interactions. Examples are customer ID or resource
ID.
• The partition key must be available in all requests, either directly or in a way that could be
easily inferred deterministically by other parameters.
2. Persistent cell mapping: Upstream services should only interact with a single cell for the
lifecycle of their resources.
• Depending on the workload, a cell migration strategy may be needed to migrate data from
one cell to another. A possible scenario when a cell migration may be needed is if a particular
user or resource in your workload becomes too big and requires it to have a dedicated cell.
• Cells should not share state or components between cells.
