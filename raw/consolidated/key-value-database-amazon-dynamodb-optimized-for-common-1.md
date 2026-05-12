---
title: "Key-value database Amazon DynamoDB Optimized for common"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 967
---

# Key-value database Amazon DynamoDB Optimized for common

access patterns, typically
to store and retrieve large
volumes of data. High-traf
fic web apps, ecommerce
systems, and gaming
applications are typical
use-cases for key-value
databases.
• Automate storage allocation: For storage systems that are a fixed size, such as Amazon EBS or
Amazon FSx, monitor the available storage space and automate storage allocation on reaching
a threshold. You can leverage Amazon CloudWatch to collect and analyze different metrics for
Amazon EBS and Amazon FSx.
• Choose the right storage class: Choose the appropriate storage class for your data.
• Amazon S3 storage classes can be configured at the object level. A single bucket can contain
objects stored across all of the storage classes.
• You can use Amazon S3 Lifecycle policies to automatically transition objects between storage
classes or remove data without any application changes. In general, you have to make a trade-
off between resource efficiency, access latency, and reliability when considering these storage
mechanisms.


# Key-value database Amazon DynamoDB Optimized for common

access patterns, typically
to store and retrieve large
volumes of data. High-traf
fic web apps, ecommerce
systems, and gaming
applications are typical
use-cases for key-value
databases.