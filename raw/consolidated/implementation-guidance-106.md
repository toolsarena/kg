---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 406
---

# Implementation guidance

Automation is a theme throughout the practices for protecting your data at rest. SEC01-
BP06 Automate deployment of standard security controls describes how you can capture the
configuration of your resources using infrastructure as code (IaC) templates, such as with AWS
CloudFormation. These templates are committed to a version control system, and are used to
deploy resources on AWS through a CI/CD pipeline. These techniques equally apply to automating
the configuration of your data storage solutions, such as encryption settings on Amazon S3
buckets.
You can check the settings that you define in your IaC templates for misconfiguration in your CI/
CD pipelines using rules in AWS CloudFormation Guard. You can monitor settings that are not yet
available in CloudFormation or other IaC tooling for misconfiguration with AWS Config. Alerts that
Config generates for misconfigurations can be remediated automatically, as described in SEC04-
BP04 Initiate remediation for non-compliant resources.
Using automation as part of your permissions management strategy is also an integral component
of automated data protections. SEC03-BP02 Grant least privilege access and SEC03-BP04 Reduce
permissions continuously describe configuring least-privilege access policies that are continually
monitored by the AWS Identity and Access Management Access Analyzer to generate findings when
permission can be reduced. Beyond automation for monitoring permissions, you can configure
Amazon GuardDuty to watch for anomalous data access behavior for your EBS volumes (by way of
an EC2 instance), S3 buckets, and supported Amazon Relational Database Service databases.
Automation also plays a role in detecting when sensitive data is stored in unauthorized locations.
SEC07-BP03 Automate identification and classification describes how Amazon Macie can monitor
your S3 buckets for unexpected sensitive data and generate alerts that can initiate an automated
response.
Follow the practices in REL09 Back up data to develop an automated data backup and recovery
strategy. Data backup and recovery is as important for recovering from security events as it is for
operational events.
