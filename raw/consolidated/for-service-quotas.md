---
title: "For Service Quotas:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 472
---

# For Service Quotas:

• Review AWS Service Quotas.
• To be aware of your existing service quotas, determine the services (like IAM Access Analyzer)
that are used. There are approximately 250 AWS services controlled by service quotas. Then,
determine the specific service quota name that might be used within each account and Region.
There are approximately 3000 service quota names per Region.
• Augment this quota analysis with AWS Config to find all AWS resources used in your AWS
accounts.
• Use AWS CloudFormation data to determine your AWS resources used. Look at the resources that
were created either in the AWS Management Console or with the list-stack-resources AWS
CLI command. You can also see resources configured to be deployed in the template itself.
• Determine all the services your workload requires by looking at the deployment code.
• Determine the service quotas that apply. Use the programmatically accessible information from
Trusted Advisor and Service Quotas.
• Establish an automated monitoring method (see REL01-BP02 Manage service quotas across
accounts and regions and REL01-BP04 Monitor and manage quotas) to alert and inform if
services quotas are near or have reached their limit.


# For Systems Manager Patch Manager:

1. Create a patch baseline.
2. Select a patching operations method.
3. Enable compliance reporting and scanning.

# For Systems Manager Patch Manager:

1. Create a patch baseline.
2. Select a patching operations method.
3. Enable compliance reporting and scanning.