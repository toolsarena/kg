---
title: "Data 973"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 978
---

# Data 973

| Service | When to use |
| --- | --- |
| Lambda@Edge | Use for compute-heavy operations that are
run when objects are not in the cache. |
| CloudFront Functions | Use for simple use cases such as HTTP(s)
request/response manipulations that can be
initiated by short-lived functions. |
| AWS IoT Greengrass | Run local compute, messaging, and data
caching for connected devices. |


# Data management

The optimal data management solution for a particular system varies based on the kind of data
type (block, file, or object), access patterns (random or sequential), required throughput, frequency