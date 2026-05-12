---
title: "SEC03-BP08 Share resources securely within your organization"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 340
---

# SEC03-BP08 Share resources securely within your organization

As the number of workloads grows, you might need to share access to resources in those workloads
or provision the resources multiple times across multiple accounts. You might have constructs
to compartmentalize your environment, such as having development, testing, and production
environments. However, having separation constructs does not limit you from being able to share
securely. By sharing components that overlap, you can reduce operational overhead and allow for
a consistent experience without guessing what you might have missed while creating the same
resource multiple times.
Desired outcome: Minimize unintended access by using secure methods to share resources within
your organization, and help with your data loss prevention initiative. Reduce your operational
overhead compared to managing individual components, reduce errors from manually creating
the same component multiple times, and increase your workloads’ scalability. You can benefit
from decreased time to resolution in multi-point failure scenarios, and increase your confidence
in determining when a component is no longer needed. For prescriptive guidance on analyzing
externally shared resources, see SEC03-BP07 Analyze public and cross-account access.
