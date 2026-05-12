---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 581
---

# Common anti-patterns:

• You deploy resources manually using the command line or at the AWS Management Console
(also known as click-ops).
• You tightly couple your application components or resources, and create inflexible architectures
as a result.
• You implement inflexible scaling policies that do not adapt to changing business requirements,
traffic patterns, or new resource types.
• You manually estimate capacity to meet anticipated demand.
Benefits of establishing this best practice: Infrastructure as code (IaC) allows infrastructure
to be defined programmatically. This helps you manage infrastructure changes through the
