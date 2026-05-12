---
title: "Using multiple Availability Zones"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 620
---

# Using multiple Availability Zones

Availability Zones are resource hosting locations that are physically separated from each other to
avoid correlated failures due to risks such as fires, floods, and tornadoes. Each Availability Zone has
independent physical infrastructure, including utility power connections, backup power sources,
mechanical services, and network connectivity. This arrangement limits faults in any of these
components to just the impacted Availability Zone. For example, if an AZ-wide incident makes EC2
instances unavailable in the affected Availability Zone, your instances in other Availability Zone
remains available.
Despite being physically separated, Availability Zones in the same AWS Region are close enough
to provide high-throughput, low-latency (single-digit millisecond) networking. You can replicate
data synchronously between Availability Zones for most workloads without significantly impacting
user experience. This means you can use Availability Zones in a Region in an active/active or active/
standby configuration.
All compute associated with your workload should be distributed among multiple Availability
Zones. This includes Amazon EC2 instances, AWS Fargate tasks, and VPC-attached AWS Lambda
functions. AWS compute services, including EC2 Auto Scaling, Amazon Elastic Container Service
(ECS), and Amazon Elastic Kubernetes Service (EKS), provide ways for you to launch and manage
compute across Availability Zones. Configure them to automatically replace compute as needed in
a different Availability Zone to maintain availability. To direct traffic to available Availability Zones,
place a load balancer in front of your compute, such as an Application Load Balancer or Network
Load Balancer. AWS load balancers can reroute traffic to available instances in the event of an
Availability Zone impairment.
