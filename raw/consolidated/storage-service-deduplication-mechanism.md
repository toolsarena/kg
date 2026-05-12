---
title: "Storage service Deduplication mechanism"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 974
---

# Storage service Deduplication mechanism

that have changed after your most recent
snapshot are saved.
• Use lifecycle policies: Use lifecycle policies to automate unneeded data deletion. Use native
service features like Amazon DynamoDB Time To Live, Amazon S3 Lifecycle, or Amazon
CloudWatch log retention for deletion.
• Use data virtualization: Use data virtualization capabilities on AWS to maintain data at its
source and avoid data duplication.
• Cloud Native Data Virtualization on AWS
• Optimize Data Pattern Using Amazon Redshift Data Sharing
• Use incremental backup: Use backup technology that can make incremental backups.
• Use native durability: Leverage the durability of Amazon S3 and replication of Amazon EBS to
meet your durability goals instead of self-managed technologies (such as a redundant array of
independent disks (RAID)).
• Use efficient logging: Centralize log and trace data, deduplicate identical log entries, and
establish mechanisms to tune verbosity when needed.
• Use efficient caching: Pre-populate caches only where justified.
• Establish cache monitoring and automation to resize the cache accordingly.
• Remove old version assets: Remove out-of-date deployments and assets from object stores and
edge caches when pushing new versions of your workload.


# Storage Storage utilization Optimized storage cost (for

example Glacier, deep archive,
or Infrequent Access) divided
by total storage cost

# Storage Storage utilization Optimized storage cost (for

example Glacier, deep archive,
or Infrequent Access) divided
by total storage cost

# Streaming storage Amazon Kinesis Efficient ingestion and

storage of streaming data.

# Streaming storage Amazon Kinesis Efficient ingestion and

storage of streaming data.

# SUS02-BP01 Scale workload infrastructure dynamically

Use elasticity of the cloud and scale your infrastructure dynamically to match supply of cloud
resources to demand and avoid overprovisioned capacity in your workload.

# SUS02-BP01 Scale workload infrastructure dynamically

Use elasticity of the cloud and scale your infrastructure dynamically to match supply of cloud
resources to demand and avoid overprovisioned capacity in your workload.

# SUS02-BP02 Align SLAs with sustainability goals

Review and optimize workload service-level agreements (SLA) based on your sustainability goals
to minimize the resources required to support your workload while continuing to meet business
needs.

# SUS02-BP02 Align SLAs with sustainability goals

Review and optimize workload service-level agreements (SLA) based on your sustainability goals
to minimize the resources required to support your workload while continuing to meet business
needs.

# SUS02-BP03 Stop the creation and maintenance of unused assets

Decommission unused assets in your workload to reduce the number of cloud resources required to
support your demand and minimize waste.

# SUS02-BP03 Stop the creation and maintenance of unused assets

Decommission unused assets in your workload to reduce the number of cloud resources required to
support your demand and minimize waste.

# SUS02-BP04 Optimize geographic placement of workloads based on their networking

requirements
Select cloud location and services for your workload that reduce the distance network traffic must
travel and decrease the total network resources required to support your workload.

# SUS02-BP04 Optimize geographic placement of workloads based on their networking

requirements
Select cloud location and services for your workload that reduce the distance network traffic must
travel and decrease the total network resources required to support your workload.

# SUS02-BP05 Optimize team member resources for activities performed

Optimize resources provided to team members to minimize the environmental sustainability
impact while supporting their needs.

# SUS02-BP05 Optimize team member resources for activities performed

Optimize resources provided to team members to minimize the environmental sustainability
impact while supporting their needs.

# SUS02-BP06 Implement buffering or throttling to flatten the demand curve

Buffering and throttling flatten the demand curve and reduce the provisioned capacity required for
your workload.

# SUS02-BP06 Implement buffering or throttling to flatten the demand curve

Buffering and throttling flatten the demand curve and reduce the provisioned capacity required for
your workload.

# SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs

Use efficient software and architecture patterns such as queue-driven to maintain consistent high
utilization of deployed resources.

# SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs

Use efficient software and architecture patterns such as queue-driven to maintain consistent high
utilization of deployed resources.

# SUS03-BP04 Optimize impact on devices and equipment

Understand the devices and equipment used in your architecture and use strategies to reduce their
usage. This can minimize the overall environmental impact of your cloud workload.

# SUS03-BP04 Optimize impact on devices and equipment

Understand the devices and equipment used in your architecture and use strategies to reduce their
usage. This can minimize the overall environmental impact of your cloud workload.

# SUS04-BP01 Implement a data classification policy

Classify data to understand its criticality to business outcomes and choose the right energy-
efficient storage tier to store the data.

# SUS04-BP01 Implement a data classification policy

Classify data to understand its criticality to business outcomes and choose the right energy-
efficient storage tier to store the data.

# SUS04-BP02 Use technologies that support data access and storage patterns

Use storage technologies that best support how your data is accessed and stored to minimize the
resources provisioned while supporting your workload.

# SUS04-BP02 Use technologies that support data access and storage patterns

Use storage technologies that best support how your data is accessed and stored to minimize the
resources provisioned while supporting your workload.

# SUS04-BP03 Use policies to manage the lifecycle of your datasets

Manage the lifecycle of all of your data and automatically enforce deletion to minimize the total
storage required for your workload.

# SUS04-BP03 Use policies to manage the lifecycle of your datasets

Manage the lifecycle of all of your data and automatically enforce deletion to minimize the total
storage required for your workload.

# SUS04-BP05 Remove unneeded or redundant data

Remove unneeded or redundant data to minimize the storage resources required to store your
datasets.

# SUS04-BP05 Remove unneeded or redundant data

Remove unneeded or redundant data to minimize the storage resources required to store your
datasets.

# SUS04-BP07 Minimize data movement across networks

Use shared file systems or object storage to access common data and minimize the total
networking resources required to support data movement for your workload.

# SUS04-BP07 Minimize data movement across networks

Use shared file systems or object storage to access common data and minimize the total
networking resources required to support data movement for your workload.

# SUS04-BP08 Back up data only when difficult to recreate

Avoid backing up data that has no business value to minimize storage resources requirements for
your workload.

# SUS04-BP08 Back up data only when difficult to recreate

Avoid backing up data that has no business value to minimize storage resources requirements for
your workload.

# SUS05-BP02 Use instance types with the least impact

Continually monitor and use new instance types to take advantage of energy efficiency
improvements.

# SUS05-BP02 Use instance types with the least impact

Continually monitor and use new instance types to take advantage of energy efficiency
improvements.

# SUS05-BP03 Use managed services

Use managed services to operate more efficiently in the cloud.

# SUS05-BP03 Use managed services

Use managed services to operate more efficiently in the cloud.

# SUS05-BP04 Optimize your use of hardware-based compute accelerators

Optimize your use of accelerated computing instances to reduce the physical infrastructure
demands of your workload.

# SUS05-BP04 Optimize your use of hardware-based compute accelerators

Optimize your use of accelerated computing instances to reduce the physical infrastructure
demands of your workload.