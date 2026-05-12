---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 551
---

# Implementation guidance

Set both a connection timeout and a request timeout on any service dependency call and generally
on any call across processes. Many frameworks offer built-in timeout capabilities, but be careful, as
some have default values that are infinite or higher than acceptable for your service goals. A value
that is too high reduces the usefulness of the timeout because resources continue to be consumed
while the client waits for the timeout to occur. A value that is too low can generate increased traffic
on the backend and increased latency because too many requests are retried. In some cases, this
can lead to complete outages because all requests are being retried.
