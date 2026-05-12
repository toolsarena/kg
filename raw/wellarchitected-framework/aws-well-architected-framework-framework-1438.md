---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 896
---

# AWS Well-Architected Framework Framework

determine the most appropriate pricing model. Often your pricing model consists of a combination
of multiple options, as determined by your availability
On-Demand Instances allow you to pay for compute or database capacity by the hour or by
the second (60 seconds minimum) depending on which instances you run, without long-term
commitments or upfront payments.
Savings Plans are a flexible pricing model that offers low prices on Amazon EC2, Lambda, and AWS
Fargate usage, in exchange for a commitment to a consistent amount of usage (measured in dollars
per hour) over one year or three years terms.
Spot Instances are an Amazon EC2 pricing mechanism that allows you request spare compute
capacity at discounted hourly rate (up to 90% off the on-demand price) without upfront
commitment.
Reserved Instances allow you up to 75 percent discount by prepaying for capacity. For more
details, see Optimizing costs with reservations.
You might choose to include a Savings Plans for the resources associated with the production,
quality, and development environments. Alternatively, because sandbox resources are only
powered on when needed, you might choose an on-demand model for the resources in that
environment. Use Amazon Spot Instances to reduce Amazon EC2 costs or use Compute Savings
Plans to reduce Amazon EC2, Fargate, and Lambda cost. The AWS Cost Explorer recommendations
tool provides opportunities for commitment discounts with Saving plans.
If you have been purchasing Reserved Instances for Amazon EC2 in the past or have established
cost allocation practices inside your organization, you can continue using Amazon EC2 Reserved
Instances for the time being. However, we recommend working on a strategy to use Savings
Plans in the future as a more flexible cost savings mechanism. You can refresh Savings Plans (SP)
Recommendations in AWS Cost Management to generate new Savings Plans Recommendations
at any time. Use Reserved Instances (RI) to reduce Amazon RDS, Amazon Redshift, Amazon
ElastiCache, and Amazon OpenSearch Service costs. Saving Plans and Reserved Instances
are available in three options: all upfront, partial upfront and no upfront payments. Use the
recommendations provided in AWS Cost Explorer RI and SP purchase recommendations.
To find opportunities for Spot workloads, use an hourly view of your overall usage, and look
for regular periods of changing usage or elasticity. You can use Spot Instances for various fault-
tolerant and flexible applications. Examples include stateless web servers, API endpoints, big data
and analytics applications, containerized workloads, CI/CD, and other flexible workloads.
