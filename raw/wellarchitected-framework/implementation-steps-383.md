---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 642
---

# Implementation steps

• Use Auto Scaling groups to deploy tiers in a workload. Auto Scaling can perform self-healing on
stateless applications and add or remove capacity.
• For compute instances noted previously, use load balancing and choose the appropriate type of
load balancer.
• Consider healing for Amazon RDS. With standby instances, configure for auto failover to the
standby instance. For Amazon RDS Read Replica, automated workflow is required to make a read
replica primary.
• Implement automatic recovery on EC2 instances that have applications deployed that cannot be
deployed in multiple locations, and can tolerate rebooting upon failures. Automatic recovery can
be used to replace failed hardware and restart the instance when the application is not capable
of being deployed in multiple locations. The instance metadata and associated IP addresses are
kept, as well as the EBS volumes and mount points to Amazon Elastic File System or File Systems
for Lustre and Windows. Using AWS OpsWorks, you can configure automatic healing of EC2
instances at the layer level.
• Implement automated recovery using AWS Step Functions and AWS Lambda when you cannot
use automatic scaling or automatic recovery, or when automatic recovery fails. When you cannot
use automatic scaling, and either cannot use automatic recovery or automatic recovery fails, you
can automate the healing using AWS Step Functions and AWS Lambda.
• Amazon EventBridge can be used to monitor and filter for events such as CloudWatch alarms
or changes in state in other AWS services. Based on event information, it can then invoke AWS
Lambda (or other targets) to run custom remediation logic on your workload.
