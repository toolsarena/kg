---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 649
---

# AWS Well-Architected Framework Framework

Availability Zone or Regional impairment), this approach is less effective because it relies on both
an operational plane, and sufficient resources being available in the unaffected zones or Regions.
Your solution should also weigh reliability against the costs needs for your workload. Static
stability architectures apply to a variety of architectures including compute instances spread across
Availability Zones, database read replica designs, Kubernetes (Amazon EKS) cluster designs, and
multi-Region failover architectures.
It is also possible to implement a more statically stable design by using more resources in each
zone. By adding more zones, you reduce the amount of additional compute you need for static
stability.
An example of bimodal behavior would be a network timeout that could cause a system to attempt
to refresh the configuration state of the entire system. This would add an unexpected load to
another component and might cause it to fail, resulting in other unexpected consequences.
This negative feedback loop impacts the availability of your workload. Instead, you can build
systems that are statically stable and operate in only one mode. A statically stable design would
do constant work and always refresh the configuration state on a fixed cadence. When a call fails,
the workload would use the previously cached value and initiate an alarm.
Another example of bimodal behavior is allowing clients to bypass your workload cache when
failures occur. This might seem to be a solution that accommodates client needs but it can
significantly change the demands on your workload and is likely to result in failures.
Assess critical workloads to determine what workloads require this type of resilience design. For
those that are deemed critical, each application component must be reviewed. Example types of
services that require static stability evaluations are:
• Compute: Amazon EC2, EKS-EC2, ECS-EC2, EMR-EC2
• Databases: Amazon Redshift, Amazon RDS, Amazon Aurora
• Storage: Amazon S3 (Single Zone), Amazon EFS (mounts), Amazon FSx (mounts)
• Load balancers: Under certain designs
