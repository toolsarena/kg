---
title: "Automate forensics"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 432
---

# Automate forensics

During a security event, your incident response team must be able to collect and analyze evidence
quickly while maintaining accuracy for the time period surrounding the event (such as capturing
logs related to a specific event or resource or collecting memory dump of an Amazon EC2
instance). It’s both challenging and time consuming for the incident response team to manually
collect the relevant evidence, especially across a large number of instances and accounts.
Additionally, manual collection can be prone to human error. For these reasons, you should develop
and implement automation for forensics as much as possible.
AWS offers a number of automation resources for forensics, which are listed in the following
Resources section. These resources are examples of forensics patterns that we have developed
and customers have implemented. While they might be a useful reference architecture to start
with, consider modifying them or creating new forensics automation patterns based on your
environment, requirements, tools, and forensics processes.
