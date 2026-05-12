---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 197
---

# AWS Well-Architected Framework Framework

scripts can be run inside a Jupyter notebook to speed up discovery. Advanced organizations have
fully automated playbooks for common issues that are auto-remediated with runbooks.
Start building your playbooks by listing common incidents that happen to your workload. Choose
playbooks for incidents that are low risk and where the root cause has been narrowed down to
a few issues to start. After you have playbooks for simpler scenarios, move on to the higher risk
scenarios or scenarios where the root cause is not well known.
Your text playbooks should be automated as your organization matures. Using services like AWS
Systems Manager Automations, flat text can be transformed into automations. These automations
can be run against your workload to speed up investigations. These automations can be activated
in response to events, reducing the mean time to discover and resolve incidents.
Customers can use AWS Systems Manager Incident Manager to respond to incidents. This service
provides a single interface to triage incidents, inform stakeholders during discovery and mitigation,
and collaborate throughout the incident. It uses AWS Systems Manager Automations to speed up
detection and recovery.
