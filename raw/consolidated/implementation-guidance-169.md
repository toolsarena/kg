---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 627
---

# Implementation guidance

If the best practice to deploy the workload to multiple locations is not possible due to
technological constraints, you must implement an alternate path to resiliency. You must automate
the ability to recreate necessary infrastructure, redeploy applications, and recreate necessary data
for these cases.
For example, Amazon EMR launches all nodes for a given cluster in the same Availability Zone
because running a cluster in the same zone improves performance of the jobs flows as it provides
a higher data access rate. If this component is required for workload resilience, then you must have
a way to redeploy the cluster and its data. Also for Amazon EMR, you should provision redundancy
in ways other than using Multi-AZ. You can provision multiple nodes. Using EMR File System
(EMRFS), data in EMR can be stored in Amazon S3, which in turn can be replicated across multiple
Availability Zones or AWS Regions.
Similarly, for Amazon Redshift, by default it provisions your cluster in a randomly selected
Availability Zone within the AWS Region that you select. All the cluster nodes are provisioned in the
same zone.
For stateful server-based workloads deployed to an on-premise data center, you can use AWS
Elastic Disaster Recovery to protect your workloads in AWS. If you are already hosted in AWS, you
can use Elastic Disaster Recovery to protect your workload to an alternative Availability Zone or
Region. Elastic Disaster Recovery uses continual block-level replication to a lightweight staging
area to provide fast, reliable recovery of on-premises and cloud-based applications.


# Implementation guidance

To adopt new technologies, fuel innovation, and keep pace with changes in demand and
responsibilities to support your workloads, continually invest in the professional growth of your
teams.