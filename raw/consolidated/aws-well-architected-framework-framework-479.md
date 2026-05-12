---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 624
---

# AWS Well-Architected Framework Framework

b. If you are using Amazon EC2 instances, use EC2 Auto Scaling to manage your instances.
Specify the subnets you chose in the previous step when you create your Auto Scaling groups.
c. If you are using AWS Fargate compute for Amazon ECS or Amazon EKS, select the subnets you
chose in the first step when you create an ECS Service, launch an ECS task, or create a Fargate
profile for EKS.
d. If you are using AWS Lambda functions that need to run in your VPC, select the subnets you
chose in the first step when you create the Lambda function. For any functions that do not
have a VPC configuration, AWS Lambda manages availability for you automatically.
e. Place traffic directors such as load balancers in front of your compute resources. If cross-
zone load balancing is enabled, AWS Application Load Balancers and Network Load
Balancers detect when targets such as EC2 instances and containers are unreachable due
to Availability Zone impairment and reroute traffic towards targets in healthy Availability
Zones. If you disable cross-zone load balancing, use Amazon Application Recovery Controller
(ARC) to provide zonal shift capability. If you are using a third-party load balancer or have
implemented your own load balancers, configure them with multiple front ends across
different Availability Zones.
4. Replicate your workload's data across multiple Availability Zones.
a. If you use an AWS-managed data service such as Amazon RDS, Amazon ElastiCache, or
Amazon FSx, study its user guide to understand its data replication and resilience capabilities.
Enable cross-AZ replication and failover if necessary.
b. If you use AWS-managed storage services such as Amazon S3, Amazon EFS, and Amazon
FSx, avoid using single-AZ or One Zone configurations for data that requires high durability.
Use a multi-AZ configuration for these services. Check the respective service's user guide to
determine whether multi-AZ replication is enabled by default or whether you must enable it.
c. If you run a self-managed database, queue, or other storage service, arrange for multi-AZ
replication according to the application's instructions or best practices. Familiarize yourself
with the failover procedures for your application.
5. Configure your DNS service to detect AZ impairment and reroute traffic to a healthy Availability
Zone. Amazon Route 53, when used in combination with Elastic Load Balancers, can do this
automatically. Route 53 can also be configured with failover records that use health checks to
respond to queries with only healthy IP addresses. For any DNS records used for failover, specify
a short time to live (TTL) value (for example, 60 seconds or less) to help prevent record caching
from impeding recovery (Route 53 alias records supply appropriate TTLs for you).
