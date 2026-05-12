---
title: "Alignment to demand 940"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 945
---

# Alignment to demand 940

| Service | When to use |
| --- | --- |
| Lambda@Edge | Use for compute-heavy operations that are
initiated when objects are not in the cache. |
| Amazon CloudFront Functions | Use for simple use cases like HTTP(s) request
or response manipulations that can be
initiated by short-lived functions. |
| AWS IoT Greengrass | Use to run local compute, messaging, and
data caching for connected devices. |
