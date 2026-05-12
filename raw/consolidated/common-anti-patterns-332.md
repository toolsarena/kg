---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 416
---

# Common anti-patterns:

• Using deprecated versions of SSL, TLS, and cipher suite components (for example, SSL v3.0,
1024-bit RSA keys, and RC4 cipher).
• Allowing unencrypted (HTTP) traffic to or from public-facing resources.
• Not monitoring and replacing X.509 certificates prior to expiration.
• Using self-signed X.509 certificates for TLS.
Level of risk exposed if this best practice is not established: High
