---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 955
---

# AWS Well-Architected Framework Framework

• Identify unused components: Identify unused or under-utilized components in your
architecture.
• For stable workloads, check AWS rightsizing tools such as AWS Compute Optimizer at regular
intervals to identify idle, unused, or underutilized components.
• For ephemeral workloads, evaluate utilization metrics to identify idle, unused, or underutilized
components.
• Remove unused components: Retire components and associated assets (like Amazon ECR
images) that are no longer needed.
• Automated Cleanup of Unused Images in Amazon ECR
• Delete unused Amazon Elastic Block Store (Amazon EBS) volumes by using AWS Config and
