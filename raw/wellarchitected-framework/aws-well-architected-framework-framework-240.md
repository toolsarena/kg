---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 324
---

# AWS Well-Architected Framework Framework

assumes that the identity provider is available, but the configuration on AWS is modified or has
expired.
• Pre-create resources needed by the emergency access process (SEC10-BP05). For example, pre-
create the emergency access AWS account with IAM users and roles, and the cross-account IAM
roles in all the workload accounts. This verifies that these resources are ready and available when
an emergency event happens. By pre-creating resources, you do not have a dependency on AWS
control plane APIs (used to create and modify AWS resources) that may be unavailable in an
emergency. Further, by pre-creating IAM resources, you do not need to account for potential
delays due to eventual consistency.
• Include emergency access processes as part of your incident management plans (SEC10-BP02).
Document how emergency events are tracked and communicated to others in your organization
such as peer teams, your leadership, and, when applicable, externally to your customers and
business partners.
• Define the emergency access request process in your existing service request workflow system
if you have one. Typically, such workflow systems allow you to create intake forms to collect
information about the request, track the request through each stage of the workflow, and
add both automated and manual approval steps. Relate each request with a corresponding
emergency event tracked in your incident management system. Having a uniform system for
emergency accesses allows you to track those requests in a single system, analyze usage trends,
and improve your processes.
• Verify that your emergency access processes can only be initiated by authorized users and
require approvals from the user's peers or management as appropriate. The approval process
should operate effectively both inside and outside business hours. Define how requests for
approval allow secondary approvers if the primary approvers are unavailable and are escalated
up your management chain until approved.
• Implement robust logging, monitoring, and alerting mechanisms for the emergency access
process and mechanisms. Generate detailed audit logs for all successful and failed attempts
to gain emergency access. Correlate the activity with ongoing emergency events from your
incident management system, and initiate alerts when actions occur outside of expected time
periods or when the emergency access account is used during normal operations. The emergency
access account should only be accessed during emergencies, as break-glass procedures can
be considered a backdoor. Integrate with your security information and event management
(SIEM) tool or AWS Security Hub CSPM to report and audit all activities during the emergency
access period. Upon returning to normal operations, automatically rotate the emergency access
credentials, and notify the relevant teams.
