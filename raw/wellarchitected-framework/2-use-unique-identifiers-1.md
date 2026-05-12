---
title: "2. Use unique identifiers"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 533
---

# 2. Use unique identifiers

Include a unique token in each idempotent operation request sent by the sender, either directly
in the request or as part of its metadata (for example, an HTTP header). This allows the receiver
to recognize and handle duplicate requests or operations. Identifiers commonly used for tokens
include Universally Unique Identifiers (UUIDs) and K-Sortable Unique Identifiers (KSUIDs).
