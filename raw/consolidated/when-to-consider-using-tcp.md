---
title: "When to consider using TCP"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 780
---

# When to consider using TCP

TCP provides reliable data delivery, and can be used for communication between workload
components where reliability and guaranteed delivery of data is important. Many web-based
applications rely on TCP-based protocols, such as HTTP and HTTPS, to open TCP sockets for
communication between application components. Email and file data transfer are common
applications that also make use of TCP, as it is a simple and reliable transfer mechanism between
application components. Using TLS with TCP can add some overhead to the communication,
which can result in increased latency and reduced throughput, but it comes with the advantage
of security. The overhead comes mainly from the added overhead of the handshake process,
which can take several round-trips to complete. Once the handshake is complete, the overhead of
encrypting and decrypting data is relatively small.
