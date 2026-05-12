---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 614
---

# AWS Well-Architected Framework Framework

2. Determine the RPO for the workload. For more detail, see REL13-BP01 Define recovery
objectives for downtime and data loss.
3. Use an automated backup solution or managed service. AWS Backup is a fully-managed
service that makes it easy to centralize and automate data protection across AWS services,
in the cloud, and on-premises. Using backup plans in AWS Backup, create rules which define
the resources to backup, and the frequency at which these backups should be created. This
frequency should be informed by the RPO established in Step 2. For hands-on guidance on how
to create automated backups using AWS Backup, see Testing Backup and Restore of Data. Native
backup capabilities are offered by most AWS services that store data. For example, RDS can be
leveraged for automated backups with point-in-time recovery (PITR).
4. For data sources not supported by an automated backup solution or managed service such as
on-premises data sources or message queues, consider using a trusted third-party solution to
create automated backups. Alternatively, you can create automation to do this using the AWS
CLI or SDKs. You can use AWS Lambda Functions or AWS Step Functions to define the logic
involved in creating a data backup, and use Amazon EventBridge to invoke it at a frequency
based on your RPO.
