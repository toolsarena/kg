---
title: "Benefits of establishing this best practice:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 299
---

# Benefits of establishing this best practice:

• Secrets are stored encrypted at rest and in transit.
• Access to credentials is gated through an API (think of it as a credential vending machine).
• Access to a credential (both read and write) is audited and logged.
• Separation of concerns: credential rotation is performed by a separate component, which can be
segregated from the rest of the architecture.
• Secrets are automatically distributed on-demand to software components and rotation occurs in
a central location.
• Access to credentials can be controlled in a fine-grained manner.
Level of risk exposed if this best practice is not established: High
