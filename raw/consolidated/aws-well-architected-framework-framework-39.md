---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 57
---

# AWS Well-Architected Framework Framework

Demand pricing. Spot Instances are appropriate where the system can tolerate using a fleet of
servers where individual servers can come and go dynamically, such as stateless web servers, batch
processing, or when using HPC and big data.
Appropriate service selection can also reduce usage and costs; such as CloudFront to minimize data
transfer, or decrease costs, such as utilizing Amazon Aurora on Amazon RDS to remove expensive
database licensing costs.
The following questions focus on these considerations for cost optimization.
COST 5: How do you evaluate cost when you select services?
Amazon EC2, Amazon EBS, and Amazon S3 are building-block AWS services. Managed services,
such as Amazon RDS and Amazon DynamoDB, are higher level, or application level, AWS
services. By selecting the appropriate building blocks and managed services, you can optimize
this workload for cost. For example, using managed services, you can reduce or remove much of
your administrative and operational overhead, freeing you to work on applications and business-
related activities.
COST 6: How do you meet cost targets when you select resource type, size and number?
Verify that you choose the appropriate resource size and number of resources for the task at
hand. You minimize waste by selecting the most cost effective type, size, and number.
COST 7: How do you use pricing models to reduce cost?
Use the pricing model that is most appropriate for your resources to minimize expense.
COST 8: How do you plan for data transfer charges?
Verify that you plan and monitor data transfer charges so that you can make architectural
decisions to minimize costs. A small yet effective architectural change can drastically reduce
your operational costs over time.
