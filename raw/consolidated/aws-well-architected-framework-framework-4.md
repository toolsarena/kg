---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 9
---

# AWS Well-Architected Framework Framework

• We think about architecture as being how components work together in a workload. How
components communicate and interact is often the focus of architecture diagrams.
• Milestones mark key changes in your architecture as it evolves throughout the product lifecycle
(design, implementation, testing, go live, and in production).
• Within an organization the technology portfolio is the collection of workloads that are required
for the business to operate.
• The level of effort is categorizing the amount of time, effort, and complexity a task requires for
implementation. Each organization needs to consider the size and expertise of the team and the
complexity of the workload for additional context to properly categorize the level of effort for
the organization.
• High: The work might take multiple weeks or multiple months. This could be broken out into
multiple stories, releases, and tasks.
• Medium: The work might take multiple days or multiple weeks. This could be broken out into
multiple releases and tasks.
• Low: The work might take multiple hours or multiple days. This could be broken out into
multiple tasks.
When architecting workloads, you make trade-offs between pillars based on your business context.
These business decisions can drive your engineering priorities. You might optimize to improve
sustainability impact and reduce cost at the expense of reliability in development environments, or,
for mission-critical solutions, you might optimize reliability with increased costs and sustainability
impact. In ecommerce solutions, performance can affect revenue and customer propensity to buy.
Security and operational excellence are generally not traded-off against the other pillars.


# AWS Well-Architected Framework Framework

By factoring in cost during service selection, and using tools such as Cost Explorer and AWS Trusted
Advisor to regularly review your AWS usage, you can actively monitor your utilization and adjust
your deployments accordingly.