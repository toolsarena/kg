---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 817
---

# AWS Well-Architected Framework Framework

• Linked or member account: An account in Organizations is a standard AWS account that
contains your AWS resources and the identities that can access those resources.
• Environment: An environment is a collection of AWS resources that runs an application version.
An environment can be made with multiple linked or member accounts.
• Project: A project is a combination of set objectives or tasks to be accomplished within a fixed
period. It is important to consider the project lifecycle during your forecast.
• AWS services: Groups or categories such as compute or storage services where you can group
AWS services for your forecast.
• Custom grouping: You can create custom groups based on your organization's needs, such as
business units, cost centers, teams, cost allocation tags, cost categories, linked accounts, or
combination of these.
Identify the business drivers that can impact your usage cost, and forecast for each of them
separately to calculate expected usage in advance. Some of the drivers might be linked to IT
and product teams within the organization. Other business drivers, such as marketing events,
promotions, geographic expansions, mergers, and acquisitions, are known by your sales, marketing,
and business leaders, and it's important to collaborate and account for all those demand drivers as
well.
You can use AWS Cost Explorer for trend-based forecasting in a defined future time range based
on your past spend. AWS Cost Explorer's forecasting engine segments your historical data based on
charge types (for example, Reserved Instances) and uses a combination of machine learning and
rule-based models to predict spend across all charge types individually.
Once you've established your forecast process and built models, you can use AWS Budgets to set
custom budgets at a granular level by specifying the time period, recurrence, or amount (fixed or
variable) and add filters such as service, AWS Region, and tags. The budget is usually prepared for a
single year and remains fixed, which requires strict adherence from everyone involved. In contrast,
forecasts are more flexible, which allows for readjustments throughout the year and provides
dynamic projections over a period of one, two, or three years. Both budgets and forecasts play
a crucial role when you establish financial expectations among various technology and business
stakeholders. Accurate forecasts and implementation also provides accountability to stakeholders
who are directly responsible for provisioning cost in the first place, and it can also raise their overall
cost awareness.
To stay informed on the performance of your existing budgets, you can create and schedule AWS
Budgets reports to email you and your stakeholders on a regular cadence. You can also create AWS
