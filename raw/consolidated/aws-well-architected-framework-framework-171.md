---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 232
---

# AWS Well-Architected Framework Framework

current service events and upcoming changes, such as planned lifecycle events, so you can take
steps to mitigate impacts.
a. Create purpose-fit AWS Health event notifications to e-mail and chat channels through AWS
User Notifications, and integrate programatically with your monitoring and alerting tools
through Amazon EventBridge or the AWS Health API.
b. Plan and track progress on health events that require action by integrating with change
management or ITSM tools (like Jira or ServiceNow) that you may already use through
Amazon EventBridge or the AWS Health API.
c. If you use AWS Organizations, enable organization view for AWS Health to aggregate AWS
Health events across accounts.
3. Integrate Amazon CloudWatch alarms with Incident Manager: Configure CloudWatch alarms
to automatically create incidents in AWS Systems Manager Incident Manager.
4. Integrate Amazon EventBridge with Incident Manager: Create EventBridge rules to react to
events and create incidents using defined response plans.


# AWS Well-Architected Framework Framework

• Preparing for incidents in Incident Manager

# AWS Well-Architected Framework Framework

• Enhances the organization's ability to maintain trust and meet regulatory requirements.
Level of risk exposed if this best practice is not established: High

# AWS Well-Architected Framework Framework

Level of risk exposed if this best practice is not established: Medium