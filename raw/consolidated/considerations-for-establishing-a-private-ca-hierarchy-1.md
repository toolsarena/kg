---
title: "Considerations for establishing a private CA hierarchy"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 413
---

# Considerations for establishing a private CA hierarchy

When you need to establish a private CA, it's important to take special care to properly design the
CA hierarchy upfront. It's a best practice to deploy each level of your CA hierarchy into separate
AWS accounts when creating a private CA hierarchy. This intentional step reduces the surface area
