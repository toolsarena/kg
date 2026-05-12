---
title: "1. Identify idempotent operations"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 533
---

# 1. Identify idempotent operations

Determine which operations require idempotency. These typically include POST, PUT, and
DELETE HTTP methods and database insert, update, or delete operations. Operations that do
not mutate state, such as read-only queries, usually do not require idempotency unless they
have side effects.
