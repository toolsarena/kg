---
title: "Client-side caching"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 760
---

# Client-side caching

With client-side caching, each client (an application or service that queries the backend datastore)
can store the results of their unique queries locally for a specified amount of time. This can reduce
the number of requests across the network to a datastore by checking the local client cache first.
If the results are not present, the application can then query the datastore and store those results
locally. This pattern allows each client to store data in the closest location possible (the client
