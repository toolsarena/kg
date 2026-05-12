---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 891
---

# AWS Well-Architected Framework Framework

guidelines whether it is an Amazon EC2 instance, AWS storage classes, or Amazon RDS instance
types. For storage resources, you can use Amazon S3 Storage Lens, which gives you visibility
into object storage usage, activity trends, and makes actionable recommendations to optimize
costs and apply data protection best practices. Using the contextual recommendations that
Amazon S3 Storage Lens derives from analysis of metrics across your organization, you can take
immediate steps to optimize your storage.
• Select resource type and size automatically based on metrics: Using the workload metrics,
manually or automatically select your workload resources. For compute resources, configuring
AWS Auto Scaling or implementing code within your application can reduce the effort required
if frequent changes are needed, and it can potentially implement changes sooner than a manual
process. You can launch and automatically scale a fleet of On-Demand Instances and Spot
Instances within a single Auto Scaling group. In addition to receiving discounts for using Spot
Instances, you can use Reserved Instances or a Savings Plan to receive discounted rates of the
regular On-Demand Instance pricing. All of these factors combined help you optimize your
cost savings for Amazon EC2 instances and determine the desired scale and performance for
your application. You can also use an attribute-based instance type selection (ABS) strategy
in Auto Scaling Groups (ASG), which lets you express your instance requirements as a set of
attributes, such as vCPU, memory, and storage. You can automatically use newer generation
instance types when they are released and access a broader range of capacity with Amazon EC2
Spot Instances. Amazon EC2 Fleet and Amazon EC2 Auto Scaling select and launch instances
that fit the specified attributes, removing the need to manually pick instance types. For storage
resources, you can use the Amazon S3 Intelligent Tiering and Amazon EFS Infrequent Access
features, which allow you to select storage classes automatically that deliver automatic storage
cost savings when data access patterns change, without performance impact or operational
overhead.
