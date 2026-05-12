---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 884
---

# AWS Well-Architected Framework Framework

review is change in usage patterns. Significant changes in usage can indicate that alternate services
would be more optimal.
If you need to move data into AWS Cloud, you can select any wide variety of services AWS offers
and partner tools to help you migrate your data sets, whether they are files, databases, machine
images, block volumes, or even tape backups. For example, to move a large amount of data to
and from AWS or process data at the edge, you can use one of the AWS purpose-built devices
to cost effectively move petabytes of data offline. Another example is for higher data transfer
rates, a direct connect service may be cheaper than a VPN which provides the required consistent
connectivity for your business.
Based on the cost analysis for different usage over time, review your scaling activity. Analyze
the result to see if the scaling policy can be tuned to add instances with multiple instance types
and purchase options. Review your settings to see if the minimum can be reduced to serve user
requests but with a smaller fleet size, and add more resources to meet the expected high demand.
Perform cost analysis for different usage over time by discussing with stakeholders in your
organization and use AWS Cost Explorer’s forecast feature to predict the potential impact of
service changes. Monitor usage level launches using AWS Budgets, CloudWatch billing alarms and
AWS Cost Anomaly Detection to identify and implement the most cost-effective services sooner.
