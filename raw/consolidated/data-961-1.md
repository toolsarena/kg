---
title: "Data 961"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 966
---

# Data 961

| Type | Technology | Key characteristics |
| --- | --- | --- |
| Archiving storage | Amazon Glacier | Storage class of Amazon S3
built for data-archiving. |
| Shared file system | Amazon Elastic File System
(Amazon EFS) | Mountable file system that
can be accessed by multiple
types of compute solutions
. Amazon EFS automatically
grows and shrinks storage
and is performance-optimi
zed to deliver consistent low
latencies. |
| Shared file system | Amazon FSx | Built on the latest AWS
compute solutions to
support four commonly used
file systems: NetApp ONTAP,
OpenZFS, Windows File
Server, and Lustre. Amazon
FSx latency, throughput, and
IOPS vary per file system
and should be considered
when selecting the right file
system for your workload
needs. |
| Block storage | Amazon Elastic Block Store
(Amazon EBS) | Scalable, high-performance
block-storage service
designed for Amazon Elastic
Compute Cloud (Amazon
EC2). Amazon EBS includes
SSD-backed storage for
transactional, IOPS-intensive
workloads and HDD-backe
d storage for throughput-
intensive workloads. |
