---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 862
---

# AWS Well-Architected Framework Framework

include representatives from all teams that own or manage an application. This certifies that
every team has access to their cost and usage information to track their consumption.
• Organize Costs Tags and Categories: organize your costs across teams, business units,
applications, environments, and projects. Use resource tags to organize costs, by cost allocation
tags. Create Cost Categories based on the dimensions by using tags, accounts, services, etc. to
map your costs.
• Configure AWS Budgets: Configure AWS Budgets on all accounts for your workloads. Set
budgets for the overall account spend, and budgets for the workloads by using tags and cost
categories. Configure notifications in AWS Budgets to receive alerts for when you exceed your
budgeted amounts, or when your estimated costs exceed your budgets.
• Configure AWS Cost Anomaly Detection: Use AWS Cost Anomaly Detection for your accounts,
core services or cost categories you created to monitor your cost and usage and detect unusual
spends. You can receive alerts individually in aggregated reports and receive alerts in an email or
an Amazon SNS topic which allows you to analyze and determine the root cause of the anomaly
and identify the factor that is driving the cost increase.
• Use cost analysis tools: Configure AWS Cost Explorer for your workload and accounts to
visualize your cost data for further analysis. Create a dashboard for the workload that tracks
overall spend, key usage metrics for the workload, and forecast of future costs based on your
historical cost data.
• Use cost-saving analysis tools: Use AWS Cost Optimization Hub to identify savings
opportunities with tailored recommendations including deleting unused resources, rightsizing,
savings Plans, reservations and compute optimizer recommendations.
• Configure advanced tools: You can optionally create visuals to facilitate interactive analysis and
sharing of cost insights. With Data Exports on AWS Cost Optimization Hub, you can create cost
and usage dashboard powered by Quick for your organization that provides additional detail
and granularity. You can also implement advanced analysis capability by using data exports in
Amazon Athena for advanced queries, and create dashboards on Quick. Work with AWS Partners
to adopt cloud management solutions for consolidated cloud bill monitoring and optimization.


# AWS Well-Architected Framework Framework

• Best Practices for Tagging AWS Resources
• Tagging your AWS resources
• AWS Cost Categories
• Analyzing your costs with AWS Budgets
• Analyzing your costs with AWS Cost Explorer
• What is AWS Data Exports?

# AWS Well-Architected Framework Framework

b. Implement a strategy that allows for automated rollback based upon pre-defined failure
conditions that result from one or more of your test methods.
8. Develop your automated test cases to allow for reusability across future repeatable changes.