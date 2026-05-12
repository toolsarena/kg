---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 983
---

# Common anti-patterns:

• You are only using one family of instances.
• You are only using x86 instances.
• You specify one instance type in your Amazon EC2 Auto Scaling configuration.
• You use AWS instances in a manner that they were not designed for (for example, you use
compute-optimized instances for a memory-intensive workload).
• You do not evaluate new instance types regularly.
• You do not check recommendations from AWS rightsizing tools such as AWS Compute Optimizer.
Benefits of establishing this best practice: By using energy-efficient and right-sized instances, you
are able to greatly reduce the environmental impact and cost of your workload.
