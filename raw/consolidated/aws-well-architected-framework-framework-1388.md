---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 841
---

# AWS Well-Architected Framework Framework

It is advised to always have at least one management account with one member account linked
to it, regardless of your organization size or usage. All workload resources should reside only
within member accounts and no resource should be created in management account. There is
no one size fits all answer for how many AWS accounts you should have. Assess your current and
future operational and cost models to ensure that the structure of your AWS accounts reflects
your organization’s goals. Some companies create multiple AWS accounts for business reasons, for
example:
• Administrative or fiscal and billing isolation is required between organization units, cost centers,
or specific workloads.
• AWS service limits are set to be specific to particular workloads.
• There is a requirement for isolation and separation between workloads and resources.
Within AWS Organizations, consolidated billing creates the construct between one or more
member accounts and the management account. Member accounts allow you to isolate and
distinguish your cost and usage by groups. A common practice is to have separate member
accounts for each organization unit (such as finance, marketing, and sales), or for each environment
lifecycle (such as development, testing and production), or for each workload (workload a, b, and
c), and then aggregate these linked accounts using consolidated billing.
Consolidated billing allows you to consolidate payment for multiple member AWS accounts under
a single management account, while still providing visibility for each linked account’s activity. As
costs and usage are aggregated in the management account, this allows you to maximize your
service volume discounts, and maximize the use of your commitment discounts (Savings Plans and
Reserved Instances) to achieve the highest discounts.
The following diagram shows how you can use AWS Organizations with organizational units (OU)
to group multiple accounts, and place multiple AWS accounts under each OU. It is recommended to
use OUs for various use cases and workloads which provides patterns for organizing accounts.


# AWS Well-Architected Framework Framework

Example of grouping multiple AWS accounts under organizational units.
AWS Control Tower can quickly set up and configure multiple AWS accounts, ensuring that
governance is aligned with your organization’s requirements.