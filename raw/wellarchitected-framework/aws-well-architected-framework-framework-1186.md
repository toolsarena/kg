---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 568
---

# AWS Well-Architected Framework Framework

You can construct customized views of metrics and alerts of your AWS resources for your teams
using CloudWatch dashboards. The customizable home pages in the CloudWatch console allow you
to monitor your resources in a single view across multiple Regions.
Alarms can perform one or more actions, like sending a notification to an Amazon SNS topic,
performing an Amazon EC2 action or an Amazon EC2 Auto Scaling action, or creating an OpsItem
or incident in AWS Systems Manager.
Amazon CloudWatch uses Amazon SNS to send notifications when the alarm changes state,
providing message delivery from the publishers (producers) to the subscribers (consumers). For
more detail on setting up Amazon SNS notifications, see Configuring Amazon SNS.
CloudWatch sends EventBridge events whenever a CloudWatch alarm is created, updated, deleted,
or its state changes. You can use EventBridge with these events to create rules that perform
actions, such as notifying you whenever the state of an alarm changes or automatically triggering
events in your account using Systems Manager automation.
Stay informed with AWS Health. AWS Health is the authoritative source of information about the
health of your AWS Cloud resources. Use AWS Health to get notified of any confirmed service
events so you can quickly take steps to mitigate any impact. Create purpose-fit AWS Health
event notifications to e-mail and chat channels through AWS User Notifications and integrate
programmatically with your monitoring and alerting tools through Amazon EventBridge. If you use
AWS Organizations, aggregate AWS Health events across accounts.
When should you use EventBridge or Amazon SNS?
Both EventBridge and Amazon SNS can be used to develop event-driven applications, and your
choice will depend on your specific needs.
Amazon EventBridge is recommended when you want to build an application that reacts to
events from your own applications, SaaS applications, and AWS services. EventBridge is the only
event-based service that integrates directly with third-party SaaS partners. EventBridge also
automatically ingests events from over 200 AWS services without requiring developers to create
any resources in their account.
EventBridge uses a defined JSON-based structure for events, and helps you create rules that are
applied across the entire event body to select events to forward to a target. EventBridge currently
supports over 20 AWS services as targets, including AWS Lambda, Amazon SQS, Amazon SNS,
Amazon Kinesis Data Streams, and Amazon Data Firehose.
