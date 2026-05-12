---
title: "Networking and content delivery 779"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 784
---

# Networking and content delivery 779

| Service | When to use |
| --- | --- |
| Amazon CloudFront | Use to cache static content such as images,
scripts, and videos, as well as dynamic
content such as API responses or web
applications. |
| Amazon ElastiCache | Use to cache content for web applications. |
| DynamoDB Accelerator | Use to add in-memory acceleration to your
DynamoDB tables. |

| Service | When to use |
| --- | --- |
| Lambda@edge | Use for compute-heavy operations that are
initiated when objects are not in the cache. |
