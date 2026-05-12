---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 360
---

# Common anti-patterns:

• You implement automation, but fail to thoroughly test and validate remediation actions. This
can result in unintended consequences, such as disrupting legitimate business operations or
causing system instability.
• You improve response times and procedures through automation, but without proper monitoring
and mechanisms that allow human intervention and judgment when needed.
• You rely solely on remediations, rather than having remediations as one part of a broader
incident response and recovery program.
Benefits of establishing this best practice: Automatic remediations can respond to
misconfigurations faster than manual processes, which helps you minimize potential business
impacts and reduce the window of opportunity for unintended uses. When you define remediations
programmatically, they are applied consistently, which reduces the risk of human error. Automation
also can handle a larger volume of alerts simultaneously, which is particularly important in
environments operating at large scale.
Level of risk exposed if this best practice is not established: Medium
