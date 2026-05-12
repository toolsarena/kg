---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 880
---

# Implementation guidance

Open source originated in the context of software development to indicate that the software
complies with certain free distribution criteria. Open source software is composed of source code
that anyone can inspect, modify, and enhance. Based on business requirements, skill of engineers,
forecasted usage, or other technology dependencies, organizations can consider using open source
software on AWS to minimize their license costs. In other words, the cost of software licenses can
be reduced through the use of open source software. This can have significant impact on workload
costs as the size of the workload scales.
Measure the benefits of licensed software against the total cost to optimize your workload. Model
any changes in licensing and how they would impact your workload costs. If a vendor changes the
cost of your database license, investigate how that impacts the overall efficiency of your workload.
Consider historical pricing announcements from your vendors for trends of licensing changes
across their products. Licensing costs may also scale independently of throughput or usage, such
as licenses that scale by hardware (CPU bound licenses). These licenses should be avoided because
costs can rapidly increase without corresponding outcomes.
For instance, operating an Amazon EC2 instance in us-east-1 with a Linux operating system allows
you to cut costs by approximately 45%, compared to running another Amazon EC2 instance that
runs on Windows.
The AWS Pricing Calculator offers a comprehensive way to compare the costs of various resources
with different license options, such as Amazon RDS instances and different database engines.
