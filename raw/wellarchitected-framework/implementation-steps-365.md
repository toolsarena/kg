---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 569
---

# Implementation steps

1. Create an alarm using Amazon CloudWatch alarms.
a. A metric alarm monitors a single CloudWatch metric or an expression dependent on
CloudWatch metrics. The alarm initiates one or more actions based on the value of the metric
or expression in comparison to a threshold over a number of time intervals. The action may
consist of sending a notification to an Amazon SNS topic, performing an Amazon EC2 action
or an Amazon EC2 Auto Scaling action, or creating an OpsItem or incident in AWS Systems
Manager.
b. A composite alarm consists of a rule expression that considers the alarm conditions of other
alarms you've created. The composite alarm only enters alarm state if all rule conditions
are met. The alarms specified in the rule expression of a composite alarm can include
metric alarms and additional composite alarms. Composite alarms can send Amazon SNS
notifications when their state changes and can create Systems Manager OpsItems or incidents
when they enter the alarm state, but they cannot perform Amazon EC2 or Auto Scaling
actions.
2. Set up Amazon SNS notifications. When creating a CloudWatch alarm, you can include an
Amazon SNS topic to send a notification when the alarm changes state.
3. Create rules in EventBridge that matches specified CloudWatch alarms. Each rule supports
multiple targets, including Lambda functions. For example, you can define an alarm that
initiates when available disk space is running low, which triggers a Lambda function through an
EventBridge rule, to clean up the space. For more detail on EventBridge targets, see EventBridge
targets.
