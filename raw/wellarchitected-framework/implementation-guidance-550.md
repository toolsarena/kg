---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 888
---

# Implementation guidance

Amazon EC2 provides a wide selection of instance types with different levels of CPU, memory,
storage, and networking capacity to fit different use cases. These instance types feature different
blends of CPU, memory, storage, and networking capabilities, giving you versatility when selecting
the right resource combination for your projects. Every instance type comes in multiple sizes,
so that you can adjust your resources based on your workload’s demands. To determine which
instance type you need, gather details about the system requirements of the application or
software that you plan to run on your instance. These details should include the following:
• Operating system
• Number of CPU cores
• GPU cores
• Amount of system memory (RAM)
• Storage type and space
• Network bandwidth requirement
Identify the purpose of compute requirements and which instance is needed, and then explore the
various Amazon EC2 instance families. Amazon offers the following instance type families:
• General Purpose
• Compute Optimized
• Memory Optimized
• Storage Optimized
• Accelerated Computing
• HPC Optimized
For a deeper understanding of the specific purposes and use cases that a particular Amazon EC2
instance family can fulfill, see AWS Instance types.
System requirements gathering is critical for you to select the specific instance family and instance
type that best serves your needs. Instance type names are comprised of the family name and the
instance size. For example, the t2.micro instance is from the T2 family and is micro-sized.
Select resource size or type based on workload and resource characteristics (for example, compute,
memory, throughput, or write intensive). This selection is typically made using cost modeling, a
