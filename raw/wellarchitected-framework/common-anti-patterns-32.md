---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 179
---

# Common anti-patterns:

• You deploy an unsuccessful change to all of production all at once. As a result, all customers are
impacted simultaneously.
• A defect introduced in a simultaneous deployment to all systems requires an emergency release.
Correcting it for all customers takes several days.
• Managing production release requires planning and participation of several teams. This puts
constraints on your ability to frequently update features for your customers.
• You perform a mutable deployment by modifying your existing systems. After discovering that
the change was unsuccessful, you are forced to modify the systems again to restore the old
version, extending your time to recovery.
Benefits of establishing this best practice: Automated deployments balance speed of roll-outs
against delivering beneficial changes consistently to customers. Limiting impact prevents costly
deployment failures and maximizes teams ability to efficiently respond to failures.
Level of risk exposed if this best practice is not established: Medium
