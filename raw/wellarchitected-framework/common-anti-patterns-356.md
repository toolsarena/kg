---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 513
---

# Common anti-patterns:

• Teams are formed around specific technical domains like UI and UX, middleware, or database
instead of specific business domains.
• Applications span domain responsibilities. Services that span bounded contexts can be more
difficult to maintain, require larger testing efforts, and require multiple domain teams to
participate in software updates.
• Domain dependencies, like domain entity libraries, are shared across services such that changes
for one service domain require changes to other service domains
