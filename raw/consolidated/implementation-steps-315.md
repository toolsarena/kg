---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 358
---

# Implementation steps

1. Identify sources for security alert information. Understand how alerts from these systems
represent identity, action, and resources to determine where correlation is possible.
2. Establish a mechanism for capturing alerts from different sources. Consider services such as
Security Hub CSPM, EventBridge, and CloudWatch for this purpose.
3. Identify sources for data correlation and enrichment. Example sources include AWS CloudTrail,
VPC Flow Logs, Route 53 Resolver logs, and infrastructure and application logs. Any or all of
these logs might be consumed through a single integration with Amazon Security Lake.
4. Integrate your alerts with your data correlation and enrichment sources to create more detailed
security event contexts and establish criticality.
a. Amazon Detective, SIEM tooling, or other third-party solutions can perform a certain level of
ingestion, correlation, and enrichment automatically.
b. You can also use AWS services to build your own. For example, you can invoke an AWS
Lambda function to run an Amazon Athena query against AWS CloudTrail or Amazon Security
Lake, and publish the results to EventBridge.
