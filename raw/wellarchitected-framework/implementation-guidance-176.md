---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 652
---

# Implementation guidance

When defining a monitoring strategy, a triggered alarm is a common event. This event would
likely contain an identifier for the alarm, the alarm state (such as IN ALARM or OK), and details
of what triggered it. In many cases, an alarm event should be detected and an email notification
sent. This is an example of an action on an alarm. Alarm notification is critical in observability,
as it informs the right people that there is an issue. However, when action on events mature in
your observability solution, it can automatically remediate the issue without the need for human
intervention.
Once KPI-monitoring alarms have been established, alerts should be sent to appropriate teams
when thresholds are exceeded. Those alerts may also be used to trigger automated processes that
will attempt to remediate the degradation.
For more complex threshold monitoring, composite alarms should be considered. Composite
alarms use a number of KPI-monitoring alarms to create an alert based on operational business
logic. CloudWatch Alarms can be configured to send emails, or to log incidents in third-party
incident tracking systems using Amazon SNS integration or Amazon EventBridge.
