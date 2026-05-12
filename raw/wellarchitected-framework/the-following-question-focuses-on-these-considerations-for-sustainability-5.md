---
title: "The following question focuses on these considerations for sustainability:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 65
---

# The following question focuses on these considerations for sustainability:

SUS 4: How do you take advantage of data management policies and patterns to support
your sustainability goals?
Implement data management practices to reduce the provisioned storage required to support
your workload, and the resources required to use it. Understand your data, and use storage
technologies and configurations that most effectively supports the business value of the data
and how it’s used. Lifecycle data to more efficient, less performant storage when requirements
decrease, and delete data that’s no longer required.
Implement a data classification policy: Classify data to understand its significance to business
outcomes. Use this information to determine when you can move data to more energy-efficient
storage or safely delete it.
Use technologies that support data access and storage patterns: Use storage that most effectively
supports how your data is accessed and stored to minimize the resources provisioned while
supporting your workload. For example, solid state devices (SSDs) are more energy intensive than
magnetic drives and should be used only for active data use cases. Use energy-efficient, archival-
class storage for infrequently accessed data.
Use lifecycle policies to delete unnecessary data: Manage the lifecycle of all your data and
automatically enforce deletion timelines to minimize the total storage requirements of your
workload.
Minimize over-provisioning in block storage: To minimize total provisioned storage, create block
storage with size allocations that are appropriate for the workload. Use elastic volumes to expand
storage as data grows without having to resize storage attached to compute resources. Regularly
review elastic volumes and shrink over-provisioned volumes to fit the current data size.
