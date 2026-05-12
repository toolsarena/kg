---
title: "When to consider using UDP"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 780
---

# When to consider using UDP

UDP is a connection-less-oriented protocol and is therefore suitable for applications that need
fast, efficient transmission, such as log, monitoring, and VoIP data. Also, consider using UDP if
you have workload components that respond to small queries from large numbers of clients to
ensure optimal performance of the workload. Datagram Transport Layer Security (DTLS) is the UDP
equivalent of Transport Layer Security (TLS). When using DTLS with UDP, the overhead comes from
encrypting and decrypting the data, as the handshake process is simplified. DTLS also adds a small
amount of overhead to the UDP packets, as it includes additional fields to indicate the security
parameters and to detect tampering.
