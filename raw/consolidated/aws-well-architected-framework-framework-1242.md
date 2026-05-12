---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 638
---

# AWS Well-Architected Framework Framework

automatically deployed to multiple Availability Zones by AWS. In case of failure, these AWS services
automatically route traffic to healthy locations. Data is redundantly stored in multiple Availability
Zones and remains available.
For Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon EKS, or Amazon ECS, Multi-AZ is
a configuration option. AWS can direct traffic to the healthy instance if failover is initiated. This
failover action may be taken by AWS or as required by the customer
For Amazon EC2 instances, Amazon Redshift, Amazon ECS tasks, or Amazon EKS pods, you choose
which Availability Zones to deploy to. For some designs, Elastic Load Balancing provides the
solution to detect instances in unhealthy zones and route traffic to the healthy ones. Elastic Load
Balancing can also route traffic to components in your on-premises data center.
For Multi-Region traffic failover, rerouting can leverage Amazon Route 53, Amazon Application
Recovery Controller, AWS Global Accelerator, Route 53 Private DNS for VPCs, or CloudFront to
provide a way to define internet domains and assign routing policies, including health checks, to
route traffic to healthy Regions. AWS Global Accelerator provides static IP addresses that act as a
fixed entry point to your application, then route to endpoints in AWS Regions of your choosing,
using the AWS global network instead of the internet for better performance and reliability.


# AWS Well-Architected Framework Framework

• For location impairment (such as Availability Zone or AWS Region), ensure you have systems in
place to fail over to healthy resources in unimpaired locations. Check quota, autoscaling levels,
and resources running before failover testing.

# AWS Well-Architected Framework Framework

• Failover with DRS