---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 383
---

# Implementation guidance

Operating system images, container images, and code artifacts are often distributed with integrity
checks available, such as through a digest or hash. These allow clients to verify integrity by
computing their own hash of the payload and validating it is the same as the one published. While
these checks help verify that the payload has not been tampered with, they do not validate the
payload came from the original source (its provenance). Verifying provenance requires a certificate
that a trusted authority issues to digitally sign the artifact.
