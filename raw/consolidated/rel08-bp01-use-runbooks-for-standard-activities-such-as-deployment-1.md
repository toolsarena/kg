---
title: "REL08-BP01 Use runbooks for standard activities such as deployment"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 591
---

# REL08-BP01 Use runbooks for standard activities such as deployment

Runbooks are the predefined procedures to achieve specific outcomes. Use runbooks to perform
standard activities, whether done manually or automatically. Examples include deploying a
workload, patching a workload, or making DNS modifications.
For example, put processes in place to ensure rollback safety during deployments. Ensuring that
you can roll back a deployment without any disruption for your customers is critical in making a
service reliable.
For runbook procedures, start with a valid effective manual process, implement it in code, and
invoke it to automatically run where appropriate.
