---
title: "Asynchronous dependency"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 522
---

# Asynchronous dependency

To temporally decouple your workload from its dependency, they should communicate
asynchronously. Using an asynchronous approach, your workload can continue with any other
processing without having to wait for its dependency, or chain of dependencies, to send a
response.
When your workload needs to communicate asynchronously with its dependency, consider the
following guidance:
• Determine whether to use messaging or event streaming based on your use case and
requirements. Messaging allows your workload to communicate with its dependency by sending
