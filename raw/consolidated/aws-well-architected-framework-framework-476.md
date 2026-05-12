---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 621
---

# AWS Well-Architected Framework Framework

You should also replicate data for your workload and make it available in multiple Availability
Zones. Some AWS managed data services, such as Amazon S3, Amazon Elastic File Service (EFS),
Amazon Aurora, Amazon DynamoDB, Amazon Simple Queue Service (SQS), and Amazon Kinesis
Data Streams replicate data in multiple Availability Zones by default and are robust against
Availability Zone impairment. With other AWS managed data services, such as Amazon Relational
Database Service (RDS), Amazon Redshift, and Amazon ElastiCache, you must enable multi-AZ
replication. Once enabled, these services automatically detect an Availability Zone impairment,
redirect requests to an available Availability Zone, and re-replicate data as needed after recovery
without customer intervention. Familiarize yourself with the user guide for each AWS managed
data service you use to understand its multi-AZ capabilities, behaviors, and operations.
If you are using self-managed storage, such as Amazon Elastic Block Store (EBS) volumes or
Amazon EC2 instance storage, you must manage multi-AZ replication yourself.
Figure 9: Multi-tier architecture deployed across three Availability Zones. Note that Amazon S3 and
Amazon DynamoDB are always Multi-AZ automatically. The ELB also is deployed to all three zones.
