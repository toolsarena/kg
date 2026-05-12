---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 354
---

# AWS Well-Architected Framework Framework

collect data from distributed sources and undergo correlation, analysis, and response workflows.
This requires managing a complex set of permissions for accessing the various data sources and
additional overhead in operating the extraction, transformation, and loading (ETL) processes.
To overcome these challenges, consider aggregating all relevant sources of security log data into
a Log Archive account as described in Organizing Your AWS Environment Using Multiple Accounts.
This includes all security-related data from your workload and logs that AWS services generate,
such as AWS CloudTrail, AWS WAF, Elastic Load Balancing, and Amazon Route 53. There are
several benefits to capturing this data in standardized locations in a separate AWS account with
proper cross-account permissions. This practice helps prevent log tampering within compromised
workloads and environments, provides a single integration point for additional tools, and offers
a more simplified model for configuring data retention and lifecycle. Evaluate the impacts of
data sovereignty, compliance scopes, and other regulations to determine if multiple security data
storage locations and retention periods are required.
To ease capturing and standardizing logs and findings, evaluate Amazon Security Lake in your
Log Archive account. You can configure Security Lake to automatically ingest data from common
sources such as CloudTrail, Route 53, Amazon EKS, and VPC Flow Logs. You can also configure AWS
Security Hub CSPM as a data source into Security Lake, allowing you to correlate findings from
other AWS services, such as Amazon GuardDuty and Amazon Inspector, with your log data. You
can also use third-party data source integrations, or configure custom data sources. All integrations
standardize your data into the Open Cybersecurity Schema Framework (OCSF) format, and are
stored in Amazon S3 buckets as Parquet files, eliminating the need for ETL processing.
Storing security data in standardized locations provides advanced analytics capabilities. AWS
recommends you deploy tools for security analytics that operate in an AWS environment into a
Security Tooling account that is separate from your Log Archive account. This approach allows
you to implement controls at depth to protect the integrity and availability of the logs and log
management process, distinct from the tools that access them. Consider using services, such as
Amazon Athena, to run on-demand queries that correlate multiple data sources. You can also
integrate visualization tools, such as Quick. AI-powered solutions are becoming increasingly
available and can perform functions such as translating findings into human-readable summaries
and natural language interaction. These solutions are often more readily integrated by having a
standardized data storage location for querying.


# AWS Well-Architected Framework Framework

• High performing organization - the Amazon Two-Pizza team
• How Cloud-Mature Enterprises Succeed