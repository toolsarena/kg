---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 921
---

# AWS Well-Architected Framework Framework

Auto Scaling policies differ and can be categorized as dynamic and scheduled scaling policies.
Dynamic policies are manual or dynamic scaling which, scheduled or predictive scaling. You can
use scaling policies for dynamic, scheduled, and predictive scaling. You can also use metrics and
alarms from Amazon CloudWatch to trigger scaling events for your workload. We recommend you
use launch templates, which allow you to access the latest features and improvements. Not all
Auto Scaling features are available when you use launch configurations. For example, you cannot
create an Auto Scaling group that launches both Spot and On-Demand Instances or that specifies
multiple instance types. You must use a launch template to configure these features. When using
launch templates, we recommended you version each one. With versioning of launch templates,
you can create a subset of the full set of parameters. Then, you can reuse it to create other versions
of the same launch template.
You can use AWS Auto Scaling or incorporate scaling in your code with AWS APIs or SDKs. This
reduces your overall workload costs by removing the operational cost from manually making
changes to your environment, and changes can be performed much faster. This also matches your
workload resourcing to your demand at any time. In order to follow this best practice and supply
resources dynamically for your organization, you should understand horizontal and vertical scaling
in the AWS Cloud, as well as the nature of the applications running on Amazon EC2 instances. It is
better for your Cloud Financial Management team to work with technical teams to follow this best
practice.
Elastic Load Balancing (Elastic Load Balancing) helps you scale by distributing demand across
multiple resources. By using ASG and Elastic Load Balancing, you can manage incoming requests
by optimally routing traffic so that no one instance is overwhelmed in an Auto Scaling group. The
requests would be distributed among all the targets of a target group in a round-robin fashion
without consideration for capacity or utilization.
Typical metrics can be standard Amazon EC2 metrics, such as CPU utilization, network throughput,
and Elastic Load Balancing observed request and response latency. When possible, you should use
a metric that is indicative of customer experience, typically a custom metric that might originate
from application code within your workload. To elaborate how to meet the demand dynamically in
this document, we will group Auto Scaling into two categories as demand-based and time-based
supply models and deep dive into each.
Demand-based supply: Take advantage of elasticity of the cloud to supply resources to meet
changing demand by relying on near real-time demand state. For demand-based supply, use APIs
or service features to programmatically vary the amount of cloud resources in your architecture.
This allows you to scale components in your architecture and increase the number of resources


# AWS Well-Architected Framework Framework

during demand spikes to maintain performance and decrease capacity when demand subsides to
reduce costs.