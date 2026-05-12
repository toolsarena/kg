---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 350
---

# AWS Well-Architected Framework Framework

Schema Framework (OCSF), which is ready for querying. Security Lake also supports other AWS
logs and logs from third-party sources.
AWS services can generate logs not captured by the basic log sources, such as Elastic Load
Balancing logs, AWS WAF logs, AWS Config recorder logs, Amazon GuardDuty findings, Amazon
Elastic Kubernetes Service (Amazon EKS) audit logs, and Amazon EC2 instance operating system
and application logs. For a full list of logging and monitoring options, see Appendix A: Cloud
capability definitions – Logging and Events of the AWS Security Incident Response Guide.
• Research logging capabilities for each AWS service and application: Each AWS service and
application provides you with options for log storage, each of which with its own retention and
life-cycle capabilities. The two most common log storage services are Amazon Simple Storage
Service (Amazon S3) and Amazon CloudWatch. For long retention periods, it is recommended to
use Amazon S3 for its cost effectiveness and flexible lifecycle capabilities. If the primary logging
option is Amazon CloudWatch Logs, as an option, you should consider archiving less frequently
accessed logs to Amazon S3.
• Select log storage: The choice of log storage is generally related to which querying tool you use,
retention capabilities, familiarity, and cost. The main options for log storage are an Amazon S3
bucket or a CloudWatch Log group.
An Amazon S3 bucket provides cost-effective, durable storage with an optional lifecycle policy.
Logs stored in Amazon S3 buckets can be queried using services such as Amazon Athena.
A CloudWatch log group provides durable storage and a built-in query facility through
CloudWatch Logs Insights.
• Identify appropriate log retention: When you use an Amazon S3 bucket or CloudWatch log
group to store logs, you must establish adequate lifecycles for each log source to optimize
storage and retrieval costs. Customers generally have between three months to one year of logs
readily available for querying, with retention of up to seven years. The choice of availability and
retention should align with your security requirements and a composite of statutory, regulatory,
and business mandates.
• Use logging for each AWS service and application with proper retention and lifecycle
policies: For each AWS service or application in your organization, look for the specific logging
configuration guidance:
• Configure AWS CloudTrail Trail
• Configure VPC Flow Logs
• Configure Amazon GuardDuty Finding Export
