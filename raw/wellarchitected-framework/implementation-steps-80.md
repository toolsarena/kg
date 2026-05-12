---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 407
---

# Implementation steps

1. Capture data storage configuration in IaC templates. Use automated checks in your CI/CD
pipelines to detect misconfigurations.
a. You can use for CloudFormation your IaC templates, and CloudFormation Guard for checking
templates for misconfiguration.
b. Use AWS Config to run rules in a proactive evaluation mode. Use this setting to check the
compliance of a resource as a step in your CI/CD pipeline before creating it.
2. Monitor resources for data storage misconfigurations.
a. Set AWS Config to monitor data storage resources for changes in control configurations and
generate alerts to invoke remediation actions when it detects a misconfiguration.
b. See SEC04-BP04 Initiate remediation for non-compliant resources for more guidance on
automated remediations.
3. Monitor and reduce data access permissions continually through automation.
a. IAM Access Analyzer can run continually to generate alerts when permissions can potentially
be reduced.
4. Monitor and alert on anomalous data access behaviors.
a. GuardDuty watches for both known threat signatures and deviations from baseline access
behaviors for data storage resources such as EBS volumes, S3 buckets, and RDS databases.
5. Monitor and alert on sensitive data being stored in unexpected locations.
a. Use Amazon Macie to continually scan your S3 buckets for sensitive data.
6. Automate secure and encrypted backups of your data.
a. AWS Backup is a managed service that creates encrypted and secure backups of various
data sources on AWS. Elastic Disaster Recovery allows you to copy full server workloads
and maintain continuous data protection with a recovery point objective (RPO) measured
in seconds. You can configure both services to work together to automate creating data
backups and copying them to failover locations. This can help keep your data available when
impacted by either operational or security events.
