---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 641
---

# Implementation guidance

Designs for Amazon EKS or other Kubernetes services should include both minimum and maximum
replica or stateful sets and the minimum cluster and node group sizing. These mechanisms provide
a minimum amount of continually-available processing resources while automatically remediating
any failures using the Kubernetes control plane.
Design patterns that are accessed through a load balancer using compute clusters should leverage
Auto Scaling groups. Elastic Load Balancing (ELB) automatically distributes incoming application
traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs).
Clustered compute-based designs that do not use load balancing should have their size designed
for loss of at least one node. This will allow for the service to maintain itself running in potentially
reduced capacity while it's recovering a new node. Example services are Mongo, DynamoDB
Accelerator, Amazon Redshift, Amazon EMR, Cassandra, Kafka, MSK-EC2, Couchbase, ELK, and
Amazon OpenSearch Service. Many of these services can be designed with additional auto healing
features. Some cluster technologies must generate an alert upon the loss a node triggering an
automated or manual workflow to recreate a new node. This workflow can be automated using
AWS Systems Manager to remediate issues quickly.
Amazon EventBridge can be used to monitor and filter for events such as CloudWatch alarms
or changes in state in other AWS services. Based on event information, it can then invoke AWS
Lambda, Systems Manager Automation, or other targets to run custom remediation logic on your
workload. Amazon EC2 Auto Scaling can be configured to check for EC2 instance health. If the
instance is in any state other than running, or if the system status is impaired, Amazon EC2 Auto
Scaling considers the instance to be unhealthy and launches a replacement instance. For large-
scale replacements (such as the loss of an entire Availability Zone), static stability is preferred for
high availability.
