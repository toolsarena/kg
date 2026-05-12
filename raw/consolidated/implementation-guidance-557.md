---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 904
---

# Implementation guidance

Performing regular cost modeling helps you implement opportunities to optimize across multiple
workloads. For example, if multiple workloads use On-Demand Instances at an aggregate level,
the risk of change is lower, and implementing a commitment-based discount can achieve a lower
overall cost. It is recommended to perform analysis in regular cycles of two weeks to one month.
This allows you to make small adjustment purchases, so the coverage of your pricing models
continues to evolve with your changing workloads and their components.
Use the AWS Cost Explorer recommendations tool to find opportunities for commitment discounts
in your management account. Recommendations at the management account level are calculated
considering usage across all of the accounts in your AWS organization that have Reserve Instances
(RI) or Savings Plans (SP). They're also calculated when discount sharing is activated to recommend
a commitment that maximizes savings across accounts.
While purchasing at the management account level optimizes for max savings in many cases, there
may be situations where you might consider purchasing SPs at the linked account level, like when
you want the discounts to apply first to usage in that particular linked account. Member account
recommendations are calculated at the individual account level, to maximize savings for each
isolated account. If your account owns both RI and SP commitments, they will be applied in this
order:
