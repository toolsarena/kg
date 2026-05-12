---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 192
---

# AWS Well-Architected Framework Framework

back to the early days of aviation. In cloud operations, we use runbooks to reduce risk and achieve
desired outcomes. At its simplest, a runbook is a checklist to complete a task.
Runbooks are an essential part of operating your workload. From onboarding a new team member
to deploying a major release, runbooks are the codified processes that provide consistent outcomes
no matter who uses them. Runbooks should be published in a central location and updated as the
process evolves, as updating runbooks is a key component of a change management process. They
should also include guidance on error handling, tools, permissions, exceptions, and escalations in
case a problem occurs.
As your organization matures, begin automating runbooks. Start with runbooks that are short and
frequently used. Use scripting languages to automate steps or make steps easier to perform. As
you automate the first few runbooks, you'll dedicate time to automating more complex runbooks.
Over time, most of your runbooks should be automated in some way.
Desired outcome: Your team has a collection of step-by-step guides for performing workload
tasks. The runbooks contain the desired outcome, necessary tools and permissions, and
instructions for error handling. They are stored in a central location (version control system) and
updated frequently. For example, your runbooks provide capabilities for your teams to monitor,
communicate, and respond to AWS Health events for critical accounts during application alarms,
operational issues, and planned lifecycle events.
