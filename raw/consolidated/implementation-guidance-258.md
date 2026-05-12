---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 902
---

# Implementation guidance

To improve cost efficiency, AWS provides multiple commitment recommendations based on your
past usage. You can use these recommendations to understand what you can save, and how the
commitment will be used. You can use these services as On-Demand, Spot, or make a commitment
for a certain period of time and reduce your on-demand costs with Reserved Instances (RIs) and
Savings Plans (SPs). You need to understand not only each workload components and multiple
AWS services, but also commitment discounts, purchase options, and Spot Instances for these
services to optimize your workload.
Consider the requirements of your workload’s components, and understand the different pricing
models for these services. Define the availability requirement of these components. Determine
if there are multiple independent resources that perform the function in the workload, and what
the workload requirements are over time. Compare the cost of the resources using the default On-
Demand pricing model and other applicable models. Factor in any potential changes in resources or
workload components.
For example, let’s look at this Web Application Architecture on AWS. This sample workload consists
of multiple AWS services, such as Amazon Route 53, AWS WAF, Amazon CloudFront, Amazon EC2
instances, Amazon RDS instances, Load Balancers, Amazon S3 storage, and Amazon Elastic File
System (Amazon EFS). You need to review each of these services, and identify potential cost saving
opportunities with different pricing models. Some of them may be eligible for RIs or SPs, while
some of them may be available only on-demand. As the following image shows, some of the AWS
services can be committed using RIs or SPs.
