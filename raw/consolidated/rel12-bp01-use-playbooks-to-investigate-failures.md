---
title: "REL12-BP01 Use playbooks to investigate failures"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 657
---

# REL12-BP01 Use playbooks to investigate failures

Permit consistent and prompt responses to failure scenarios that are not well understood,
by documenting the investigation process in playbooks. Playbooks are the predefined steps
performed to identify the factors contributing to a failure scenario. The results from any process
step are used to determine the next steps to take until the issue is identified or escalated.
The playbook is proactive planning that you must do, to be able to take reactive actions effectively.
When failure scenarios not covered by the playbook are encountered in production, first address
the issue (put out the fire). Then go back and look at the steps you took to address the issue and
use these to add a new entry in the playbook.
Note that playbooks are used in response to specific incidents, while runbooks are used to achieve
specific outcomes. Often, runbooks are used for routine activities and playbooks are used to
respond to non-routine events.
