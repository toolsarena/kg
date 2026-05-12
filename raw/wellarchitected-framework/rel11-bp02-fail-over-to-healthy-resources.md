---
title: "REL11-BP02 Fail over to healthy resources"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 636
---

# REL11-BP02 Fail over to healthy resources

If a resource failure occurs, healthy resources should continue to serve requests. For location
impairments (such as Availability Zone or AWS Region), ensure that you have systems in place to
fail over to healthy resources in unimpaired locations.
When designing a service, distribute load across resources, Availability Zones, or Regions.
Therefore, failure of an individual resource or impairment can be mitigated by shifting traffic to
remaining healthy resources. Consider how services are discovered and routed to in the event of a
failure.
Design your services with fault recovery in mind. At AWS, we design services to minimize the
time to recover from failures and impact on data. Our services primarily use data stores that
acknowledge requests only after they are durably stored across multiple replicas within a Region.
They are constructed to use cell-based isolation and use the fault isolation provided by Availability
Zones. We use automation extensively in our operational procedures. We also optimize our replace-
and-restart functionality to recover quickly from interruptions.
The patterns and designs that allow for the failover vary for each AWS platform service. Many
AWS native managed services are natively multiple Availability Zone (like Lambda or API Gateway).
Other AWS services (like EC2 and EKS) require specific best practice designs to support failover of
resources or data storage across AZs.
