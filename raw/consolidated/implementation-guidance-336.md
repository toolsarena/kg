---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 193
---

# Implementation guidance

Runbooks can take several forms depending on the maturity level of your organization. At a
minimum, they should consist of a step-by-step text document. The desired outcome should
be clearly indicated. Clearly document necessary special permissions or tools. Provide detailed
guidance on error handling and escalations in case something goes wrong. List the runbook
owner and publish it in a central location. Once your runbook is documented, validate it by having
someone else on your team run it. As procedures evolve, update your runbooks in accordance with
your change management process.
Your text runbooks should be automated as your organization matures. Using services like
AWS Systems Manager automations, you can transform flat text into automations that can be
run against your workload. These automations can be run in response to events, reducing the
operational burden to maintain your workload. AWS Systems Manager Automation also provides a
low-code visual design experience to create automation runbooks more easily.
