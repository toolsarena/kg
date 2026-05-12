---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 897
---

# Implementation steps

• Analyze workload elasticity: Using the hourly granularity in Cost Explorer or a custom
dashboard, analyze your workload's elasticity. Look for regular changes in the number of
instances that are running. Short duration instances are candidates for Spot Instances or Spot
Fleet.
• Well-Architected Lab: Cost Explorer
• Well-Architected Lab: Cost Visualization
• Review existing pricing contracts: Review current contracts or commitments for long term
needs. Analyze what you currently have and how much those commitments are in use.
Leverage pre-existing contractual discounts or enterprise agreements. Enterprise Agreements
give customers the option to tailor agreements that best suit their needs. For long term
commitments, consider reserved pricing discounts, Reserved Instances or Savings Plans for the
specific instance type, instance family, AWS Region, and Availability Zones.
• Perform a commitment discount analysis: Using Cost Explorer in your account, review the
Savings Plans and Reserved Instance recommendations. To verify that you implement the correct
recommendations with the required discounts and risk, follow the Well-Architected labs.
