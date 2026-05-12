---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 982
---

# Implementation steps

• Choose the instances type: Choose the right instances type to best fit your needs. To learn about
how to choose Amazon Elastic Compute Cloud instances and use mechanisms such as attribute-
based instance selection, see the following:
• How do I choose the appropriate Amazon EC2 instance type for my workload?
• Attribute-based instance type selection for Amazon EC2 Fleet.
• Create an Auto Scaling group using attribute-based instance type selection.
• Scale: Use small increments to scale variable workloads.
• Use multiple compute purchase options: Balance instance flexibility, scalability, and cost
savings with multiple compute purchase options.
• Amazon EC2 On-Demand Instances are best suited for new, stateful, and spiky workloads
which can’t be instance type, location, or time flexible.
• Amazon EC2 Spot Instances are a great way to supplement the other options for applications
that are fault tolerant and flexible.
• Leverage Compute Savings Plans for steady state workloads that allow flexibility if your needs
(like AZ, Region, instance families, or instance types) change.
• Use instance and Availability Zone diversity: Maximize application availability and take
advantage of excess capacity by diversifying your instances and Availability Zones.
• Rightsize instances: Use the rightsizing recommendations from AWS tools to make
adjustments on your workload. For more information, see Optimizing your cost with Rightsizing
