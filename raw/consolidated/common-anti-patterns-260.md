---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 176
---

# Common anti-patterns:

• During production releases, untested deployments cause frequent issues that require
troubleshooting and escalation.
• Your release contains infrastructure as code (IaC) that updates existing resources. You are unsure
if the IaC runs successfully or causes impact to the resources.
• You deploy a new feature to your application. It doesn't work as intended and there is no
visibility until it gets reported by impacted users.
• You update your certificates. You accidentally install the certificates to the wrong components,
which goes undetected and impacts website visitors because a secure connection to the website
can't be established.
