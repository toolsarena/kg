---
title: "SEC09-BP01 Implement secure key and certificate management"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 412
---

# SEC09-BP01 Implement secure key and certificate management

Transport Layer Security (TLS) certificates are used to secure network communications and
establish the identity of websites, resources, and workloads over the internet, as well as private
networks.
Desired outcome: A secure certificate management system that can provision, deploy, store, and
renew certificates in a public key infrastructure (PKI). A secure key and certificate management
mechanism prevents certificate private key material from disclosure and automatically renews
the certificate on a periodic basis. It also integrates with other services to provide secure network
communications and identity for machine resources inside of your workload. Key material should
never be accessible to human identities.
