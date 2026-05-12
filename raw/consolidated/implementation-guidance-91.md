---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 364
---

# Implementation guidance

When designing a workload architecture, it is common to separate components into different
layers based on their responsibility. For example, a web application can have a presentation layer,
application layer, and data layer. You can take a similar approach when designing your
network topology. Underlying network controls can help enforce your workload's data access
requirements. For example, in a three-tier web application architecture, you can store your static
presentation layer files on Amazon S3 and serve them from a content delivery network (CDN), such
as Amazon CloudFront. The application layer can have public endpoints that an Application Load
Balancer (ALB) serves in an Amazon VPC public subnet (similar to a demilitarized zone, or DMZ),
with back-end services deployed into private subnets. The data layer, that is hosting resources such
as databases and shared file systems, can reside in different private subnets from the resources of
your application layer. At each of these layer boundaries (CDN, public subnet, private subnet), you
can deploy controls that allow only authorized traffic to traverse across those boundaries.
Similar to modeling network layers based on the functional purpose of your workload's
components, also consider the sensitivity of the data being processed. Using the web application
example, while all of your workload services may reside within the application layer, different
services may process data with different sensitivity levels. In this case, dividing the application layer
using multiple private subnets, different VPCs in the same AWS account, or even different VPCs
in different AWS accounts for each level of data sensitivity may be appropriate according to your
control requirements.
A further consideration for network layers is the behavior consistency of your workload's
components. Continuing the example, in the application layer you may have services that accept
inputs from end-users or external system integrations that are inherently riskier than the inputs to
other services. Examples include file uploads, code scripts to run, email scanning and so on. Placing
these services in their own network layer helps create a stronger isolation boundary around them,
and can prevent their unique behavior from creating false positive alerts in inspection systems.
As part of your design, consider how using AWS managed services influences your network
topology. Explore how services such as Amazon VPC Lattice can help make the interoperability of
your workload components across network layers easier. When using AWS Lambda, deploy in your
