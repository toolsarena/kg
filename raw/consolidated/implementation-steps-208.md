---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 894
---

# Implementation steps

• Evaluate existing resources: Review existing workloads that use similar services for your
workload. Depending on the workload’s components, consider existing platforms if business
logic or technical requirement allow.
• Use resource sharing in AWS RAM and restrict accordingly: Use AWS RAM to share resources
with other AWS accounts within your organization. When you share resources, you don’t need
to duplicate resources in multiple accounts, which minimizes the operational burden of resource
maintenance. This process also helps you securely share the resources that you have created with
roles and users in your account, as well as with other AWS accounts.
• Tag resources: Tag resources that are candidates for cost reporting and categorize them within
cost categories. Activate these cost related resource tags for cost allocation to provide visibility
of AWS resources usage. Focus on creating an appropriate level of granularity with respect to
cost and usage visibility, and influence cloud consumption behaviors through cost allocation
reporting and KPI tracking.
