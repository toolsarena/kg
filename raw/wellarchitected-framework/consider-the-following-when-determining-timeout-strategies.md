---
title: "Consider the following when determining timeout strategies:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 551
---

# Consider the following when determining timeout strategies:

• Requests may take longer than normal to process because of their content, impairments in a
target service, or a networking partition failure.
• Requests with abnormally expensive content could consume unnecessary server and client
resources. In this case, timing out these requests and not retrying can preserve resources.
