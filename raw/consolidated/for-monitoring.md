---
title: "For monitoring:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 484
---

# For monitoring:

• Capture current resource consumption (for example, buckets or instances). Use service API
operations, such as the Amazon EC2 DescribeInstances API, to collect current resource
consumption.
• Capture your current quotas that are essential and applicable to the services using:
• AWS Service Quotas
• AWS Trusted Advisor
• AWS documentation
• AWS service-specific pages
• AWS Command Line Interface (AWS CLI)
• AWS Cloud Development Kit (AWS CDK)
• Use AWS Service Quotas, an AWS service that helps you manage your quotas for over 250 AWS
services from one location.
• Use Trusted Advisor service limits to monitor your current service limits at various thresholds.
• Use the service quota history (console or AWS CLI) to check on regional increases.
• Compare service quota changes in each Region and each account to create equivalency, if
required.
