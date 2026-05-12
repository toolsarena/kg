---
title: "Configuration option Examples"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 751
---

# Configuration option Examples

Offloading reads (like read replicas and • For DynamoDB tables, you can offload
caching) reads using DAX for caching.
• You can create an Amazon ElastiCac
he (Redis OSS) cluster and configure
your application to read from the cache
first, falling back to the database if the
requested item is not present.
• Relational databases such as Amazon
