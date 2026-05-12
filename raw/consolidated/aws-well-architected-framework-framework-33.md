---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 48
---

# AWS Well-Architected Framework Framework

of access (online, offline, archival), frequency of update (WORM, dynamic), and availability and
durability constraints. Well-Architected workloads use purpose-built data stores which allow
different features to improve performance.
In AWS, storage is available in three forms: object, block, and file:
• Object storage provides a scalable, durable platform to make data accessible from any internet
location for user-generated content, active archive, serverless computing, Big Data storage or
backup and recovery. Amazon Simple Storage Service (Amazon S3) is an object storage service
that offers industry-leading scalability, data availability, security, and performance. Amazon S3
is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications
for companies all around the world.
• Block storage provides highly available, consistent, low-latency block storage for each virtual
host and is analogous to direct-attached storage (DAS) or a Storage Area Network (SAN). Amazon
Elastic Block Store (Amazon EBS) is designed for workloads that require persistent storage
accessible by EC2 instances that helps you tune applications with the right storage capacity,
performance and cost.
• File storage provides access to a shared file system across multiple systems. File storage
solutions like Amazon Elastic File System (Amazon EFS) are ideal for use cases such as large
content repositories, development environments, media stores, or user home directories.
Amazon FSx makes it efficient and cost effective to launch and run popular file systems so
you can leverage the rich feature sets and fast performance of widely used open source and
commercially-licensed file systems.
The following question focuses on these considerations for performance efficiency.
PERF 3: How do you store, manage, and access data in your workload?
The more efficient storage solution for a system varies based on the kind of access operation
(block, file, or object), patterns of access (random or sequential), required throughput, frequency
of access (online, offline, archival), frequency of update (WORM, dynamic), and availability and
durability constraints. Well-architected systems use multiple storage solutions and turn on
different features to improve performance and use resources efficiently.


# AWS Well-Architected Framework Framework

• Logging strategies for security incident response
• SEC04-BP01 Configure service and application logging

# AWS Well-Architected Framework Framework

• Threat Detection and Response with Amazon GuardDuty and Amazon Detective
• Security Hub Workshop
• Vulnerability Management with Amazon Inspector