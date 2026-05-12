---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 695
---

# AWS Well-Architected Framework Framework

3. Assess the resources of your workload, and what their configuration will be in the recovery
Region prior to failover (during normal operation).
For infrastructure and AWS resources use infrastructure as code such as AWS CloudFormation
or third-party tools like Hashicorp Terraform. To deploy across multiple accounts and Regions
with a single operation you can use AWS CloudFormation StackSets. For Multi-site active/
active and Hot Standby strategies, the deployed infrastructure in your recovery Region has
the same resources as your primary Region. For Pilot Light and Warm Standby strategies, the
deployed infrastructure will require additional actions to become production ready. Using
CloudFormation parameters and conditional logic, you can control whether a deployed stack is
active or standby with a single template. When using Elastic Disaster Recovery, the service will
replicate and orchestrate the restoration of application configurations and compute resources.
All DR strategies require that data sources are backed up within the AWS Region, and then those
backups are copied to the recovery Region. AWS Backup provides a centralized view where
you can configure, schedule, and monitor backups for these resources. For Pilot Light, Warm
Standby, and Multi-site active/active, you should also replicate data from the primary Region
to data resources in the recovery Region, such as Amazon Relational Database Service (Amazon
RDS) DB instances or Amazon DynamoDB tables. These data resources are therefore live and
ready to serve requests in the recovery Region.
To learn more about how AWS services operate across Regions, see this blog series on Creating a
Multi-Region Application with AWS Services.
4. Determine and implement how you will make your recovery Region ready for failover when
needed (during a disaster event).
For multi-site active/active, failover means evacuating a Region, and relying on the remaining
active Regions. In general, those Regions are ready to accept traffic. For Pilot Light and Warm
Standby strategies, your recovery actions will need to deploy the missing resources, such as the
EC2 instances in Figure 20, plus any other missing resources.
For all of the above strategies you may need to promote read-only instances of databases to
become the primary read/write instance.
For backup and restore, restoring data from backup creates resources for that data such as EBS
volumes, RDS DB instances, and DynamoDB tables. You also need to restore the infrastructure
and deploy code. You can use AWS Backup to restore data in the recovery Region. See REL09-
BP01 Identify and back up all data that needs to be backed up, or reproduce the data from
