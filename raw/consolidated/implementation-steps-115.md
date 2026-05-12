---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 572
---

# Implementation steps

1. Create an inventory of alarms: To obtain a list of all alarms, you can use the AWS CLI using the
Amazon CloudWatch command describe-alarms. Depending upon how many alarms you
have set up, you might have to use pagination to retrieve a subset of alarms for each call, or
alternatively you can use the AWS SDK to obtain the alarms using an API call.
2. Document all alarm actions: Update a runbook with all alarms and their actions, irrespective if
they are manual or automated. AWS Systems Manager provides predefined runbooks. For more
information about runbooks, see Working with runbooks. For detail on how to view runbook
content, see View runbook content.
3. Set up and manage alarm actions: For any of the alarms that require an action, specify the
automated action using the CloudWatch SDK. For example, you can change the state of your
Amazon EC2 instances automatically based on a CloudWatch alarm by creating and enabling
actions on an alarm or disabling actions on an alarm.
You can also use Amazon EventBridge to respond automatically to system events, such as
application availability issues or resource changes. You can create rules to indicate which events
you're interested in, and the actions to take when an event matches a rule. The actions that can
be automatically initiated include invoking an AWS Lambda function, invoking Amazon EC2 Run
Command, relaying the event to Amazon Kinesis Data Streams, and seeing Automate Amazon
EC2 using EventBridge.
4. Standard Operating Procedures (SOPs): Based on your application components, AWS Resilience
Hub recommends multiple SOP templates. You can use these SOPs to document all the
processes an operator should follow in case an alert is raised. You can also construct a SOP
based on Resilience Hub recommendations, where you need an Resilience Hub application
with an associated resiliency policy, as well as a historic resiliency assessment against that
application. The recommendations for your SOP are produced by the resiliency assessment.
Resilience Hub works with Systems Manager to automate the steps of your SOPs by providing a
number of SSM documents you can use as the basis for those SOPs. For example, Resilience Hub
may recommend an SOP for adding disk space based on an existing SSM automation document.
5. Perform automated actions using Amazon DevOps Guru: You can use Amazon DevOps Guru
to automatically monitor application resources for anomalous behavior and deliver targeted
recommendations to speed up problem identification and remediation times. With DevOps Guru,
you can monitor streams of operational data in near real time from multiple sources including
Amazon CloudWatch metrics, AWS Config, AWS CloudFormation, and AWS X-Ray. You can
