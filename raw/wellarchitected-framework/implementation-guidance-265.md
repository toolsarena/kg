---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 919
---

# Implementation guidance

There are several ways for AWS customers to increase the resources available to their applications
and supply resources to meet the demand. One of these options is to use AWS Instance Scheduler,
which automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and
Amazon Relational Database Service (Amazon RDS) instances. The other option is to use AWS Auto
Scaling, which allows you to automatically scale your computing resources based on the demand
of your application or service. Supplying resources based on demand will allow you to pay for the
resources you use only, reduce cost by launching resources when they are needed, and terminate
them when they aren't.
AWS Instance Scheduler allows you to configure the stop and start of your Amazon EC2 and
Amazon RDS instances at defined times so that you can meet the demand for the same resources
within a consistent time pattern such as every day user access Amazon EC2 instances at eight in
the morning that they don’t need after six at night. This solution helps reduce operational cost by
stopping resources that are not in use and starting them when they are needed.
