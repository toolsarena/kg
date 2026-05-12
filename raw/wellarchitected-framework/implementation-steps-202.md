---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 879
---

# Implementation steps

• Perform a thorough analysis: Using the component list, work through each component from
the highest priority to the lowest priority. For the higher priority and more costly components,
perform additional analysis and assess all available options and their long term impact. For lower
priority components, assess if changes in usage would change the priority of the component, and
then perform an analysis of appropriate effort.
• Compare managed and unmanaged resources: Consider the operational cost for the resources
you manage and compare them with AWS managed resources. For example, review your
databases running on Amazon EC2 instances and compare with Amazon RDS options (an AWS
managed service) or Amazon EMR compared to running Apache Spark on Amazon EC2. When
moving from a self-managed workload to a AWS fully managed workload, research your options
carefully. The three most important factors to consider are the type of managed service you
want to use, the process you will use to migrate your data and understand the AWS shared
responsibility model.
