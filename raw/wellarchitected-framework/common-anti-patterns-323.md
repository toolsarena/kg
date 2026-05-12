---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 385
---

# Common anti-patterns:

• Following the practice of immutable infrastructure, but not having a solution in place for
emergency patching or replacement of production systems.
• Using automation to fix misconfigured resources, but not having a manual override mechanism
in place. Situations may arise where you need to adjust the requirements, and you may need to
suspend automations until you make these changes.
Benefits of establishing this best practice: Automation can reduce the risk of unauthorized access
and use of your compute resources. It helps to prevent misconfigurations from making their way
into production environments, and detecting and fixing misconfigurations should they occur.
Automation also helps to detect unauthorized access and use of compute resources to reduce your
time to respond. This in turn can reduce the overall scope of impact from the issue.
Level of risk exposed if this best practice is not established: Medium
