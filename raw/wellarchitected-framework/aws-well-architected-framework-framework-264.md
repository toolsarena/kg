---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 351
---

# AWS Well-Architected Framework Framework

• Configure AWS Config recording
• Configure AWS WAF web ACL traffic
• Configure AWS Network Firewall network traffic logs
• Configure Elastic Load Balancing access logs
• Configure Amazon Route 53 resolver query logs
• Configure Amazon RDS logs
• Configure Amazon EKS Control Plane logs
• Configure Amazon CloudWatch agent for Amazon EC2 instances and on-premises servers
• Select and implement querying mechanisms for logs: For log queries, you can use CloudWatch
Logs Insights for data stored in CloudWatch log groups, and Amazon Athena and Amazon
OpenSearch Service for data stored in Amazon S3. You can also use third-party querying tools
such as a security information and event management (SIEM) service.
The process for selecting a log querying tool should consider the people, process, and
technology aspects of your security operations. Select a tool that fulfills operational, business,
and security requirements, and is both accessible and maintainable in the long term. Keep in
mind that log querying tools work optimally when the number of logs to be scanned is kept
within the tool’s limits. It is not uncommon to have multiple querying tools because of cost or
technical constraints.
For example, you might use a third-party security information and event management (SIEM)
tool to perform queries for the last 90 days of data, but use Athena to perform queries beyond
90 days because of the log ingestion cost of a SIEM. Regardless of the implementation, verify
that your approach minimizes the number of tools required to maximize operational efficiency,
especially during a security event investigation.
• Use logs for alerting: AWS provides alerting through several security services:
• AWS Config monitors and records your AWS resource configurations and allows you to
automate the evaluation and remediation against desired configurations.
• Amazon GuardDuty is a threat detection service that continually monitors for malicious
activity and unauthorized behavior to protect your AWS accounts and workloads. GuardDuty
ingests, aggregates, and analyzes information from sources, such as AWS CloudTrail
management and data events, DNS logs, VPC Flow Logs, and Amazon EKS Audit logs.
GuardDuty pulls independent data streams directly from CloudTrail, VPC Flow Logs, DNS
query logs, and Amazon EKS. You don’t have to manage Amazon S3 bucket policies or modify
