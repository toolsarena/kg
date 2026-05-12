---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 944
---

# Implementation steps

• Analyze network access patterns in your workload to identify how users use your application.
• Use monitoring tools, such as Amazon CloudWatch and AWS CloudTrail, to gather data on
network activities.
• Analyze the data to identify the network access pattern.
• Select the Regions for your workload deployment based on the following key elements:
• Your Sustainability goal: as explained in Region selection.
• Where your data is located: For data-heavy applications (such as big data and machine
learning), application code should run as close to the data as possible.
• Where your users are located: For user-facing applications, choose a Region (or Regions) close
to your workload’s users.
• Other constraints: Consider constraints such as cost and compliance as explained in What to
Consider when Selecting a Region for your Workloads.
• Use local caching or AWS Caching Solutions for frequently used assets to improve performance,
reduce data movement, and lower environmental impact.
