---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 616
---

# Implementation steps

1. Identify data sources that are currently being backed up and where these backups are being
stored. For implementation guidance, see REL09-BP01 Identify and back up all data that needs
to be backed up, or reproduce the data from sources.
2. Establish criteria for data validation for each data source. Different types of data will have
different properties which might require different validation mechanisms. Consider how this
data might be validated before you are confident to use it in production. Some common ways to
validate data are using data and backup properties such as data type, format, checksum, size, or
a combination of these with custom validation logic. For example, this might be a comparison of
the checksum values between the restored resource and the data source at the time the backup
was created.
3. Establish RTO and RPO for restoring the data based on data criticality. For implementation
guidance, see REL13-BP01 Define recovery objectives for downtime and data loss.
4. Assess your recovery capability. Review your backup and restore strategy to understand if
it can meet your RTO and RPO, and adjust the strategy as necessary. Using AWS Resilience
Hub, you can run an assessment of your workload. The assessment evaluates your application
configuration against the resiliency policy and reports if your RTO and RPO targets can be met.
5. Do a test restore using currently established processes used in production for data restoration.
These processes depend on how the original data source was backed up, the format and storage
location of the backup itself, or if the data is reproduced from other sources. For example, if
you are using a managed service such as AWS Backup, this might be as simple as restoring the
