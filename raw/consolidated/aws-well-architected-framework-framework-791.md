---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 56
---

# AWS Well-Architected Framework Framework

COST 4: How do you decommission resources?
Implement change control and resource management from project inception to end-of-life. This
facilitates shutting down unused resources to reduce waste.
You can use cost allocation tags to categorize and track your AWS usage and costs. When you apply
tags to your AWS resources (such as EC2 instances or S3 buckets), AWS generates a cost and usage
report with your usage and your tags. You can apply tags that represent organization categories
(such as cost centers, workload names, or owners) to organize your costs across multiple services.
Verify that you use the right level of detail and granularity in cost and usage reporting and
monitoring. For high level insights and trends, use daily granularity with AWS Cost Explorer. For
deeper analysis and inspection use hourly granularity in AWS Cost Explorer, or Amazon Athena and
Amazon Quick with the Cost and Usage Report (CUR) at an hourly granularity.
Combining tagged resources with entity lifecycle tracking (employees, projects) makes it
possible to identify orphaned resources or projects that are no longer generating value to the
organization and should be decommissioned. You can set up billing alerts to notify you of
predicted overspending.
