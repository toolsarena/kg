---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 698
---

# Implementation guidance

A pattern to avoid is developing recovery paths that are rarely exercised. For example, you might
have a secondary data store that is used for read-only queries. When you write to a data store and
the primary fails, you might want to fail over to the secondary data store. If you don’t frequently
