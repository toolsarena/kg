---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 972
---

# AWS Well-Architected Framework Framework

• Choose the right storage class, performance mode, and throughput mode for your file system to
address your business need, not exceeding that.
• Amazon EFS performance
• Amazon EBS volume performance on Linux instances
• Set target levels of utilization for your data volumes, and resize volumes outside of expected
ranges.
• Right size read-only volumes to fit the data.
• Migrate data to object stores to avoid provisioning the excess capacity from fixed volume sizes
on block storage.
• Regularly review elastic volumes and file systems to terminate idle volumes and shrink over-
provisioned resources to fit the current data size.
