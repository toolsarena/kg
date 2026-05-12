---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 920
---

# AWS Well-Architected Framework Framework

Cost optimization with AWS Instance Scheduler.
You can also easily configure schedules for your Amazon EC2 instances across your accounts
and Regions with a simple user interface (UI) using AWS Systems Manager Quick Setup. You can
schedule Amazon EC2 or Amazon RDS instances with AWS Instance Scheduler and you can stop
and start existing instances. However, you cannot stop and start instances which are part of your
Auto Scaling group (ASG) or that manage services such as Amazon Redshift or Amazon OpenSearch
Service. Auto Scaling groups have their own scheduling for the instances in the group and these
instances are created.
AWS Auto Scaling helps you adjust your capacity to maintain steady, predictable performance
at the lowest possible cost to meet changing demand. It is a fully managed and free service to
scale the capacity of your application that integrates with Amazon EC2 instances and Spot Fleets,
Amazon ECS, Amazon DynamoDB, and Amazon Aurora. Auto Scaling provides automatic resource
discovery to help find resources in your workload that can be configured, it has built-in scaling
strategies to optimize performance, costs, or a balance between the two, and provides predictive
scaling to assist with regularly occurring spikes.
There are multiple scaling options available to scale your Auto Scaling group:
• Maintain current instance levels at all times
• Scale manually
• Scale based on a schedule
• Scale based on demand
• Use predictive scaling
