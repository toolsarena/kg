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
