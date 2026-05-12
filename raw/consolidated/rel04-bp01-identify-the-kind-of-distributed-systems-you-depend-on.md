---
title: "REL04-BP01 Identify the kind of distributed systems you depend on"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 520
---

# REL04-BP01 Identify the kind of distributed systems you depend on

Distributed systems can be synchronous, asynchronous, or batch. Synchronous systems must
process requests as quickly as possible and communicate with each other by making synchronous
request and response calls using HTTP/S, REST, or remote procedure call (RPC) protocols.
Asynchronous systems communicate with each other by exchanging data asynchronously through
an intermediary service without coupling individual systems. Batch systems receive a large volume
of input data, run automated data processes without human intervention, and generate output
data.
Desired outcome: Design a workload that effectively interacts with synchronous, asynchronous,
and batch dependencies.
