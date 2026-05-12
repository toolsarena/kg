---
title: "DynamoDB additionally support automated backup that allows point-in-time recovery (PITR),"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 606
---

# DynamoDB additionally support automated backup that allows point-in-time recovery (PITR),

which allows you to restore a backup to any time up to five minutes or less before the current
time. Many AWS services offer the ability to copy backups to another AWS Region. AWS Backup is
a tool that gives you the ability to centralize and automate data protection across AWS services.
AWS Elastic Disaster Recovery allows you to copy full server workloads and maintain continuous
data protection from on-premise, cross-AZ or cross-Region, with a Recovery Point Objective (RPO)
measured in seconds.
Amazon S3 can be used as a backup destination for self-managed and AWS-managed data sources.
AWS services such as Amazon EBS, Amazon RDS, and Amazon DynamoDB have built in capabilities
to create backups. Third-party backup software can also be used.
On-premises data can be backed up to the AWS Cloud using AWS Storage Gateway or AWS
DataSync. Amazon S3 buckets can be used to store this data on AWS. Amazon S3 offers multiple
storage tiers such as Amazon Glacier or Amazon Glacier Deep Archive to reduce cost of data
storage.
You might be able to meet data recovery needs by reproducing the data from other sources.
For example, Amazon ElastiCache replica nodes or Amazon RDS read replicas could be used to
reproduce data if the primary is lost. In cases where sources like this can be used to meet your
Recovery Point Objective (RPO) and Recovery Time Objective (RTO), you might not require a
backup. Another example, if working with Amazon EMR, it might not be necessary to backup your
HDFS data store, as long as you can reproduce the data into Amazon EMR from Amazon S3.
