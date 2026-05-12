---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 924
---

# Implementation steps

• Configure scheduled scaling: For predictable changes in demand, time-based scaling can
provide the correct number of resources in a timely manner. It is also useful if resource
creation and configuration is not fast enough to respond to changes on demand. Using the
workload analysis configure scheduled scaling using AWS Auto Scaling. To configure time-
based scheduling, you can use predictive scaling of scheduled scaling to increase the number
of Amazon EC2 instances in your Auto Scaling groups in advance according to expected or
predictable load changes.
• Configure predictive scaling: Predictive scaling allows you to increase the number of Amazon
EC2 instances in your Auto Scaling group in advance of daily and weekly patterns in traffic flows.
If you have regular traffic spikes and applications that take a long time to start, you should
consider using predictive scaling. Predictive scaling can help you scale faster by initializing
capacity before projected load compared to dynamic scaling alone, which is reactive in nature.
For example, if users start using your workload with the start of the business hours and don’t use
after hours, then predictive scaling can add capacity before the business hours which eliminates
delay of dynamic scaling to react to changing traffic.
• Configure dynamic automatic scaling: To configure scaling based on active workload metrics,
use Auto Scaling. Use the analysis and configure Auto Scaling to launch on the correct resource
levels, and verify that the workload scales in the required time. You can launch and automatically
scale a fleet of On-Demand Instances and Spot Instances within a single Auto Scaling group.
In addition to receiving discounts for using Spot Instances, you can use Reserved Instances or a
Savings Plan to receive discounted rates of the regular On-Demand Instance pricing. All of these
factors combined help you to optimize your cost savings for Amazon EC2 instances and help you
get the desired scale and performance for your application.
