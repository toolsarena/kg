---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 607
---

# Implementation steps

1. Identify all data sources for the workload. Data can be stored on a number of resources such
as databases, volumes, filesystems, logging systems, and object storage. Refer to the Resources
section to find Related documents on different AWS services where data is stored, and the
backup capability these services provide.
2. Classify data sources based on criticality. Different data sets will have different levels of
criticality for a workload, and therefore different requirements for resiliency. For example, some
data might be critical and require a RPO near zero, while other data might be less critical and
can tolerate a higher RPO and some data loss. Similarly, different data sets might have different
RTO requirements as well.
3. Use AWS or third-party services to create backups of the data. AWS Backup is a managed
service that allows creating backups of various data sources on AWS. AWS Elastic Disaster
Recovery handles automated sub-second data replication to an AWS Region. Most AWS services
also have native capabilities to create backups. The AWS Marketplace has many solutions that
provide these capabilites as well. Refer to the Resources listed below for information on how to
create backups of data from various AWS services.
4. For data that is not backed up, establish a data reproduction mechanism. You might choose
not to backup data that can be reproduced from other sources for various reasons. There might
be a situation where it is cheaper to reproduce data from sources when needed rather than
creating a backup as there may be a cost associated with storing backups. Another example is
where restoring from a backup takes longer than reproducing the data from sources, resulting
in a breach in RTO. In such situations, consider tradeoffs and establish a well-defined process
for how data can be reproduced from these sources when data recovery is necessary. For
example, if you have loaded data from Amazon S3 to a data warehouse (like Amazon Redshift),
or MapReduce cluster (like Amazon EMR) to do analysis on that data, this may be an example
of data that can be reproduced from other sources. As long as the results of these analyses are
either stored somewhere or reproducible, you would not suffer a data loss from a failure in the
data warehouse or MapReduce cluster. Other examples that can be reproduced from sources
include caches (like Amazon ElastiCache) or RDS read replicas.
5. Establish a cadence for backing up data. Creating backups of data sources is a periodic process
and the frequency should depend on the RPO.
