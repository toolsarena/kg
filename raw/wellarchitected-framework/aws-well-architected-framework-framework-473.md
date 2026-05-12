---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 617
---

# AWS Well-Architected Framework Framework

backup into a new resource. If you used AWS Elastic Disaster Recovery you can launch a recovery
drill.
6. Validate data recovery from the restored resource based on criteria you previously established
for data validation. Does the restored and recovered data contain the most recent record or item
at the time of backup? Does this data fall within the RPO for the workload?
7. Measure time required for restore and recovery and compare it to your established RTO. Does
this process fall within the RTO for the workload? For example, compare the timestamps from
when the restoration process started and when the recovery validation completed to calculate
how long this process takes. All AWS API calls are timestamped and this information is available
in AWS CloudTrail. While this information can provide details on when the restore process
started, the end timestamp for when the validation was completed should be recorded by your
validation logic. If using an automated process, then services like Amazon DynamoDB can be
used to store this information. Additionally, many AWS services provide an event history which
provides timestamped information when certain actions occurred. Within AWS Backup, backup
and restore actions are referred to as jobs, and these jobs contain timestamp information as part
of its metadata which can be used to measure time required for restoration and recovery.
8. Notify stakeholders if data validation fails, or if the time required for restoration and recovery
exceeds the established RTO for the workload. When implementing automation to do this,
such as in this lab, services like Amazon Simple Notification Service (Amazon SNS) can be used
to send push notifications such as email or SMS to stakeholders. These messages can also be
published to messaging applications such as Amazon Chime, Slack, or Microsoft Teams or used
to create tasks as OpsItems using AWS Systems Manager OpsCenter.
9. Automate this process to run periodically. For example, services like AWS Lambda or a State
Machine in AWS Step Functions can be used to automate the restore and recovery processes,
and Amazon EventBridge can be used to invoke this automation workflow periodically as shown
in the architecture diagram below. Learn how to Automate data recovery validation with AWS
Backup. Additionally, this Well-Architected lab provides a hands-on experience on one way to do
automation for several of the steps here.
