---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 383
---

# Common anti-patterns:

• Trusting reputable vendor websites to obtain software artifacts, but ignoring certificate
expiration notices. Proceeding with downloads without confirming certificates are valid.
• Validating vendor website certificates, but not cryptographically verifying downloaded artifacts
from these websites.
• Relying solely on digests or hashes to validate software integrity. Hashes establish that artifacts
have not been modified from the original version, but do not validate their source.
• Not signing your own software, code, or libraries, even when only used in your own
deployments.
Benefits of establishing this best practice: Validating the integrity of artifacts that your workload
depends on helps prevent malware from entering your compute environments. Signing your
software helps safeguard against unauthorized running in your compute environments. Secure
your software supply chain by signing and verifying code.
Level of risk exposed if this best practice is not established: Medium
