---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 151
---

# Common anti-patterns:

• You deploy a new software change without any tests. It fails to run in production, which leads to
an outage.
• New security groups are deployed with AWS CloudFormation without being tested in a pre-
production environment. The security groups make your app unreachable for your customers.
• A method is modified but there are no unit tests. The software fails when it is deployed to
production.
Benefits of establishing this best practice: Change fail rate of software deployments are reduced.
Software quality is improved. Developers have increased awareness on the viability of their
code. Security policies can be rolled out with confidence to support organization's compliance.
Infrastructure changes such as automatic scaling policy updates are tested in advance to meet
traffic needs.
Level of risk exposed if this best practice is not established: High
