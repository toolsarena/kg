---
title: "Credential type Description Suggested strategy"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 301
---

# Credential type Description Suggested strategy

Application and database Passwords – plain text string Rotate: Store credentials in
credentials AWS Secrets Manager and
establish automated rotation
if possible.
Amazon RDS and Aurora Passwords – plain text string Replace: Use the Secrets
